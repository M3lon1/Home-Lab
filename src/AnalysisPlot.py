import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import pyqtgraph as pg
from pulse.pulsesensor import Pulsesensor
from grove.grove_gsr_sensor import GroveGSRSensor
from PilotStudie import *
import csv
import numpy as np

class AnalysisPlot(QMainWindow):
    def __init__(self, csv_path):
        """
        this class plots a csv file
        """
        super().__init__()
        self.layout = QVBoxLayout()
        self.pen = pg.mkPen(color=(255,255,255), width=2) # Style of the plot
        self.plot = pg.PlotWidget(title='Skin Conductance') # Title
        self.plot.setAccessibleName('plot_gsr') # # Name property of plot_hr
        self.plot.setBackground('#212121') # Background color
        if csv_path[-1] == '0':
            self.plot.setLabel('left', 'BPM') # y axis label
        if csv_path[-1] == '1':
            self.plot.setLabel('left', 'Micro  Siemens') # y axis label
        
        self.x = []
        self.y = []
        with open(csv_path) as csv_file:
            c = csv.reader(csv_file, delimiter=',')
            for i in c:
                print("i: ", i)
                print("csv file", len(i))

                for j in range(len(i)):
                    split = i[j].split(', ')
                    self.x.append(float(split[1].replace(']', '')))
                    self.y.append(float(split[0].replace('[', '')))
            #self.line_ref.setData(self.x, self.y)
        self.layout.addWidget(self.plot)
        self.plot.plot(self.x, self.y, pen=self.pen, symbol='o') # Symbol to use for data point
        
        
        widget = QWidget()
        widget.setLayout(self.layout)
        widget.setStyleSheet('''
        QWidget {background-color: #1c1c1c}
        ''')
        self.setCentralWidget(widget)
        self.showMaximized()
        
        
def main():
    app = QApplication(sys.argv)
    win = AnalysisPlot('results/1126211')

    
    sys.exit(app.exec_())
    
if __name__ == "__main__":
    main()