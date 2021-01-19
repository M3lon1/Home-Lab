from pulsesensor import Pulsesensor
import time

def get_heartbeat():
    p = Pulsesensor()
    p.startAsyncBPM()

    try:
        while True:
            bpm = p.BPM
            if bpm > 0:
                yield int(bpm)
            else:
                yield bpm
            time.sleep(1)
    except:
        p.stopAsyncBPM()
