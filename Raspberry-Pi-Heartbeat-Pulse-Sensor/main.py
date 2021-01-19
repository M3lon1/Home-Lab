from sensors import get_heartbeat

s = get_heartbeat()

while True:
    print(next(s))
