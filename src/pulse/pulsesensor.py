# extended from https://github.com/WorldFamousElectronics/PulseSensor_Amped_Arduino

import time
import math
import threading
from pulse.MCP3008 import MCP3008
import matplotlib.pyplot as plt
import csv

class Pulsesensor:
    def __init__(self, channel = 0, bus = 0, device = 0):
        self.channel = channel
        self.BPM = 0
        self.adc = MCP3008(bus, device)
        self.BPM_list = [] #[value, time stamp, time difference to last peak]

    def getBPMLoop(self):
        # init variables
        start_time = time.time()
        tmp_time = time.time()
        delta = 0
        rate = [0] * 10         # array to hold last 10 IBI values
        sampleCounter = 0       # used to determine pulse timing
        lastBeatTime = 0        # used to find IBI
        P = 512                 # used to find peak in pulse wave, seeded
        T = 512                 # used to find trough in pulse wave, seeded
        thresh = 525            # used to find instant moment of heart beat, seeded
        amp = 100               # used to hold amplitude of pulse waveform, seeded
        firstBeat = True        # used to seed rate array so we startup with reasonable BPM
        secondBeat = False      # used to seed rate array so we startup with reasonable BPM

        IBI = 600               # int that holds the time interval between beats! Must be seeded!
        Pulse = False           # "True" when User's live heartbeat is detected. "False" when not a "live beat". 
        lastTime = int(time.time()*1000)
        
        while not self.thread.stopped:
            Signal = self.adc.read(self.channel)
            currentTime = int(time.time()*1000)
            
            sampleCounter += currentTime - lastTime
            lastTime = currentTime
            
            N = sampleCounter - lastBeatTime

            # find the peak and trough of the pulse wave
            if Signal < thresh and N > (IBI/5.0)*3:     # avoid dichrotic noise by waiting 3/5 of last IBI
                if Signal < T:                          # T is the trough
                    T = Signal                          # keep track of lowest point in pulse wave 

            if Signal > thresh and Signal > P:
                P = Signal

            # signal surges up in value every time there is a pulse
            if N > 250:                                 # avoid high frequency noise
                if Signal > thresh and Pulse == False and N > (IBI/5.0)*3:       
                    Pulse = True                        # set the Pulse flag when we think there is a pulse
                    IBI = sampleCounter - lastBeatTime  # measure time between beats in mS
                    lastBeatTime = sampleCounter        # keep track of time for next pulse

                    if secondBeat:                      # if this is the second beat, if secondBeat == TRUE
                        secondBeat = False;             # clear secondBeat flag
                        for i in range(len(rate)):      # seed the running total to get a realisitic BPM at startup
                          rate[i] = IBI

                    if firstBeat:                       # if it's the first time we found a beat, if firstBeat == TRUE
                        firstBeat = False;              # clear firstBeat flag
                        secondBeat = True;              # set the second beat flag
                        continue

                    # keep a running total of the last 10 IBI values  
                    rate[:-1] = rate[1:]                # shift data in the rate array
                    rate[-1] = IBI                      # add the latest IBI to the rate array
                    runningTotal = sum(rate)            # add upp oldest IBI values

                    runningTotal /= len(rate)           # average the IBI values 
                    x = 60000/runningTotal
                    if not self.BPM_list or self.BPM_list[-1][0] != x:
                        try:
                            delta = (time.time() - tmp_time) * 1000
                            tmp_time = time.time()
                        except:
                            pass
                        #check if RR interval fits between standard values
                        if not 300 < delta < 1500:
                            delta = 0
                        self.BPM_list.append([int(x), tmp_time - start_time, delta])
                    
            if Signal < thresh and Pulse == True:       # when the values are going down, the beat is over
                Pulse = False                           # reset the Pulse flag so we can do it again
                amp = P - T                             # get amplitude of the pulse wave
                thresh = amp/2 + T                      # set thresh at 50% of the amplitude
                P = thresh                              # reset these for next time
                T = thresh

            if N > 2500:                                # if 2.5 seconds go by without a beat
                thresh = 512                            # set thresh default
                P = 512                                 # set P default
                T = 512                                 # set T default
                lastBeatTime = sampleCounter            # bring the lastBeatTime up to date        
                firstBeat = True                        # set these to avoid noise
                secondBeat = False                      # when we get the heartbeat back
                self.BPM = 0

            time.sleep(0.005)
            
        
    # Start getBPMLoop routine which saves the BPM in its variable
    def startAsyncBPM(self):
        self.thread = threading.Thread(target=self.getBPMLoop)
        self.thread.stopped = False
        self.thread.start()
        return
        
    # Stop the routine
    def stopAsyncBPM(self):
        self.thread.stopped = True
        self.BPM = 0
        return

    def get_SDNN(self):
        '''
        Calculates SDNN (Standard Deviation of NN intervals)
        depending on measurement time
        '''
        s = 0
        rs = 0
        for item in self.BPM_list:
            s += item[2]
        avg = s / len(self.BPM_list)
        for item in self.BPM_list:
            if item[2] != 0:
                rs += ((item[2] - avg)*(item[2] - avg))
        if len(self.BPM_list) > 1:
            hrv = math.sqrt(1/(len(self.BPM_list)-1) * rs)
            return int(hrv)
        else:
            return 0
        
    def get_RMSSD(self):
        '''
        Calculates RMSSD
        '''
        if len(self.BPM_list) > 1:
            s = 0
            for i in range(len(self.BPM_list) - 1):
                if self.BPM_list[i][2] != 0 and self.BPM_list[i+1][2] != 0:
                    s += ((self.BPM_list[i+1][2] - self.BPM_list[i][2])*(self.BPM_list[i+1][2] - self.BPM_list[i][2]))
                else:
                    pass
            rmssd = math.sqrt(1/(len(self.BPM_list)-1) * s)
            return int(rmssd)
    
    def plot(self):
        plt.style.use('fivethirtyeight')
        x_val = []
        y_val = []
        for i in range(len(self.BPM_list)):
            x_val.append(self.BPM_list[i][-2])
            y_val.append(self.BPM_list[i][0])
        plt.plot(x_val, y_val)
        plt.tight_layout()
        plt.show()
    
    def save(self, path):
        with open(path, 'w', newline="") as f:
            writer = csv.writer(f)
            writer.writerows(self.BPM_list)
            