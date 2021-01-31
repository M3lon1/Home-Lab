import math
import sys
import time
import threading
from grove.adc import ADC
 
 
class GroveGSRSensor:
 
    def __init__(self, channel = 0):
        self.channel = channel
        self.adc = ADC()
        self.GSR = 0
        self.gsr_list = []
        
    def getGSR(self):
        while not self.thread.stopped:
            self.GSR = self.adc.read(self.channel)
    
    def saveGSRList(self):
        while not self.thread.stopped:
            value = self.adc.read(self.channel)
            self.GSR = value
    
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


