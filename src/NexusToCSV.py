import sys
import csv

path = "results/PilotStudie/Proband_5/23.04/one_hand/nexus_raw.txt"
output = "results/PilotStudie/Proband_5/23.04/one_hand/nexus"
out = []
case = 2

# If time format 00:00:00
if case == 1:
    with open(path) as file:
        for line in file:
            time = line[0:8]
            hour = float(time[0:2])
            minute = float(time[3:5])
            second = float(time[6:8])
            t = second + 60 * minute + 60 * hour
            tmp = line[8:]
            value = tmp.split()
            out.append([value[0], t])

# if time format 0
if case == 2:
    with open(path) as file:
        for line in file:
            x = line.split()
            out.append([x[1], x[0]])

with open(output, 'w', newline='') as myfile:
    wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
    #wr.writerows(self.pulse_sensor.BPM_list)
    print("writing")
    wr.writerows(out)
