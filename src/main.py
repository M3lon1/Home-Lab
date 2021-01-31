from pulse.pulsesensor import *
from grove.grove_gsr_sensor import *
import datetime

# Initialize Sensor, start async Thread and get initial BPM value
pulse_sensor = Pulsesensor()
pulse_sensor.startAsyncBPM()
bpm = pulse_sensor.BPM

gsr_sensor = GroveGSRSensor()
gsr_sensor.startAsyncGSR()
gsr = gsr_sensor.GSR

# Loop to get values
while True:
    # BPM 
    if bpm != pulse_sensor.BPM:
        bpm = pulse_sensor.BPM
        sdnn = pulse_sensor.get_SDNN()
        rmssd = pulse_sensor.get_RMSSD()
        print("---Pulse Data---")
        print("BPM List: ", pulse_sensor.BPM_list[-1])
        print("BPM: ", bpm)
        print("SDNN: ", sdnn)
        print("RMSSD: ", rmssd)
    
    # GSR
    if gsr != gsr_sensor.GSR:
        gsr = gsr_sensor.GSR
        print("GSR: ", gsr)
        print("GSR List: ", gsr_sensor.GSR_list[-1])