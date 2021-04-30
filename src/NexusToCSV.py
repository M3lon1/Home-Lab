import sys
import csv
'''
This file converts nexus raw data to a data format that can be used by the AnalysisPlot.py file
The header and last line gets removed, so just the pure values stay
'''
path = "results/PilotStudie/proband_5/30.04/one_hand/nexus_raw_4.txt"
output = "results/PilotStudie/proband_5/30.04/one_hand/nexus_4"
out = []

header = 0
with open(path) as file:
    for line in file:
        if header > 14 and len(line) != 33 and len(line) != 1:
            x = line.split()
            try:
                out.append([x[1], x[0]])
            except:
                print("couldnt append: ", line)
        else:
            header += 1

with open(output, 'w', newline='') as myfile:
    wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
    print("writing")
    wr.writerows(out)
