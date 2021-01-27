from pulsesensor import Pulsesensor
import time
import datetime
import math

hb_list = []

def get_heartbeat():
    '''
    Function starts a thread to get heart beat
    yields a list with 3 items:
        [heart rate, time stamp (y, m, d ,h ,min, sec, microsec), time delta to last peak(in seconds)]
    '''
    p = Pulsesensor()
    p.startAsyncBPM()
    
    try:
        while True:
            bpm = p.BPM
            t = datetime.datetime.now()
            delta = 0
            if bpm > 0:
                if not hb_list or hb_list[-1][0] != bpm:
                    try:
                        delta = t - hb_list[-1][1]
                        delta = delta.total_seconds() * 1000
                    except:
                        pass
                    if not 300 < delta < 1500:
                        delta = 0
                    hb_list.append([bpm, t, delta])
                    yield [bpm, t, delta]
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
        return hrv
    else:
        return 0
    
def get_RMSSD():
    '''
    Calculates RMSSD
    Problem
    '''
    if len(hb_list) > 1:
        s = 0
        for i in range(len(hb_list) - 1):
            if hb_list[i][2] != 0 and hb_list[i+1][2] != 0:
                s += ((hb_list[i+1][2] - hb_list[i][2])*(hb_list[i+1][2] - hb_list[i][2]))
            else:
                pass
        rmssd = math.sqrt(1/(len(hb_list)-1) * s)
        return rmssd
        
        
        