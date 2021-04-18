import sys
import csv

path = "results/Rebecca/result_nexus_adjusted.txt"
path2 = "results/Rebecca/04224001"
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

with open("results/result_nexus_csv", 'w', newline='') as myfile:
    wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
    #wr.writerows(self.pulse_sensor.BPM_list)
    print("writing")
    wr.writerows(out)
