from sensors import *
import datetime

#s = get_heartbeat()
g = get_GSR()
print("hello")
#c = GroveGSRSensor()
#c.startAsyncGSR()


while True:
    print("------")
    

    #print("GSR", next(g))
    print(g)
    #x = next(s)
    #print("Heartbeat: ", x[0])
    #print("SDNN: ", get_SDNN(), "ms")
    #print("RMSSD: ", get_RMSSD(), "ms")
    
    #print(c.gsr_list)