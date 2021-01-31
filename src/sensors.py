from pulsesensor import Pulsesensor
from grove_gsr_sensor import GroveGSRSensor
import time
import datetime
import math

hb_list = []
gsr_list = []

def get_heartbeat():
    '''
    Function starts a thread to get heart beat
    yields a list with 3 items:
        [heart rate, time stamp (y, m, d ,h ,min, sec, microsec), time delta to last peak(in seconds)]
    '''
    p = Pulsesensor()
    p.startAsyncBPM()
    start_time = time.time()
    tmp_time = time.time()
    try:
        while True:
            bpm = p.BPM
            delta = 0
            if bpm > 0:
                if not hb_list or hb_list[-1][0] != bpm:
                    try:
                        delta = (time.time() - tmp_time) * 1000
                        tmp_time = time.time()
                    except:
                        pass
                    #check if rr interval fits between standard values
                    if not 300 < delta < 1500:
                        delta = 0
                    hb_list.append([bpm, tmp_time - start_time, delta])
                    yield [int(bpm), tmp_time - start_time, delta]
            else:
                pass
            #time.sleep(1)
    except:
        p.stopAsyncBPM()

def save_heartbeat(location):
    pass
    

def get_SDNN():
    '''
    Calculates SDNN (Standard Deviation of NN intervals)
    depending on measurement time
    '''
    s = 0
    rs = 0
    for item in hb_list:
        s += item[2]
    avg = s / len(hb_list)
    for item in hb_list:
        if item[2] != 0:
            rs += ((item[2] - avg)*(item[2] - avg))
    if len(hb_list) > 1:
        hrv = math.sqrt(1/(len(hb_list)-1) * rs)
        return int(hrv)
    else:
        return 0
    
def get_RMSSD():
    '''
    Calculates RMSSD
    '''
    if len(hb_list) > 1:
        s = 0
        for i in range(len(hb_list) - 1):
            if hb_list[i][2] != 0 and hb_list[i+1][2] != 0:
                s += ((hb_list[i+1][2] - hb_list[i][2])*(hb_list[i+1][2] - hb_list[i][2]))
            else:
                pass
        rmssd = math.sqrt(1/(len(hb_list)-1) * s)
        return int(rmssd)
        
        
def get_GSR():
    '''
    '''
    c = GroveGSRSensor()
    c.startAsyncGSR()
    try:
        while True:
            gsr_list.append(c.GSR)
    except:
        c.stopAsyncGSR
        return gsr_list
