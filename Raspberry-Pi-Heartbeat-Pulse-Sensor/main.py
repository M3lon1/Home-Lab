from sensors import *
import datetime

s = get_heartbeat()

while True:
    print("------")
    x = next(s)
    print("tupel", x)
    print("Heartbeat: ", x[0])
    print("SDNN: ", get_SDNN(), "milliseconds")
    print("RMSSD: ", get_RMSSD())
    