import math
import sys
import time
import threading
from grove.adc import ADC
import matplotlib.pyplot as plt
 
class GroveGSRSensor:
 
    def __init__(self, channel = 0):
        self.channel = channel
        self.adc = ADC()
        self.GSR = 0
        self.GSR_list = []
        
    
    def saveGSRList(self):
        start_time = time.time()
        tmp_time = time.time()
        while not self.thread.stopped:
            signal = self.adc.read(self.channel)
            try:
                value = 1/(((1024 + 2 * signal) * 10000) / (512 - signal))
            except ZeroDivisionError as e:
                pass
            self.GSR = value
            if not self.GSR_list or self.GSR_list[-1][0] != value:
                self.GSR_list.append([value, time.time() - start_time])
    
    def startAsyncGSR(self):
        self.thread = threading.Thread(target=self.saveGSRList)
        self.thread.stopped = False
        self.thread.start()
        return
    
    # Stop the routine
    def stopAsyncGSR(self):
        self.thread.stopped = True
        self.GSR = 0
        return

    def plot(self):
        plt.style.use('fivethirtyeight')
        x_val = []
        y_val = []
        for i in range(len(self.GSR_list)):
            x_val.append(self.GSR_list[i][-1])
            y_val.append(self.GSR_list[i][-2])
        plt.plot(x_val, y_val)
        plt.tight_layout()
        plt.show()
    