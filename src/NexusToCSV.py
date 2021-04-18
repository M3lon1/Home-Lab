import sys
import csv

path = "results/Rebecca/result_nexus.txt"
path2 = "results/Rebecca/04224001"
out = []
with open(path) as file:
    for line in file:
        time = line[0:8]
        tmp = line[8:]
        value = tmp.split()
        out.append([value[0], time])

with open("results/result_nexus_csv", 'w', newline='') as myfile:
    wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
    #wr.writerows(self.pulse_sensor.BPM_list)
    print("writing")
    wr.writerows(out)
