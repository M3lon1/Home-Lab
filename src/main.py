from pulse.pulsesensor import Pulsesensor
from grove.grove_gsr_sensor import GroveGSRSensor
import datetime
import tkinter as tk


# root window 
root = tk.Tk()
width = root.winfo_screenwidth()
height = root.winfo_screenheight()
root.geometry(f'{width}x{height}')
root.title("PsyMex-2")

# Heart Rate Window
hr_window = tk.Frame(root, width=width, height = height/2, highlightbackground="black", highlightthickness=1)
hr_window.pack_propagate(0)
hr_window.pack(side="top")
lbl_hr = tk.Label(hr_window, text="Heart Rate", font=("Arial Bold", 20))
lbl_hr.pack(padx=lbl_hr.winfo_width()/2)

# Heart Rate Window
gsr_window = tk.Frame(root, width=width, height=height/2, highlightbackground="black", highlightthickness=1)
gsr_window.pack_propagate(0)
gsr_window.pack(side="top")
lbl_gsr = tk.Label(gsr_window, text="Skin Conductance", font=("Arial Bold", 20))
lbl_gsr.pack(padx=lbl_gsr.winfo_width()/2)


root.mainloop()

"""
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
        '''
        # GSR
        if gsr != gsr_sensor.GSR:
            gsr = gsr_sensor.GSR
            print("---GSR Data---")
            print("GSR: ", gsr, "siemens")
        '''
    except KeyboardInterrupt:
        # interrupt with ctrl + c
        pulse_sensor.save("out.csv")
        gsr_sensor.plot()
        pulse_sensor.plot()
        pulse_sensor.stopAsyncBPM()
        gsr_sensor.stopAsyncGSR()
        interrupt = True
        
"""