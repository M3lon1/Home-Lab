from pulse.pulsesensor import Pulsesensor
from grove.grove_gsr_sensor import GroveGSRSensor
import datetime

# Initialize Sensor, start async Thread and get initial BPM value
# Pulse Sensor
pulse_sensor = Pulsesensor()
pulse_sensor.startAsyncBPM()
bpm = pulse_sensor.BPM
# GSR Sensor
gsr_sensor = GroveGSRSensor()
gsr_sensor.startAsyncGSR()
gsr = gsr_sensor.GSR
interrupt = False

# Loop to get values
while not interrupt:
    try:
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
            print("GSR: ", gsr, "siemens")
            
    except KeyboardInterrupt:
        pulse_sensor.stopAsyncBPM()
        gsr_sensor.stopAsyncGSR()
        interrupt = True