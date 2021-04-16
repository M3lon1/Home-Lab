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
        
        # a used to reduce gsr datapoints that are plotted
        a = 0
        self.x = []
        self.y = []
        with open(csv_path) as csv_file:
            c = csv.reader(csv_file, delimiter=',')
            for i in c:
                
                a += 1
                #print("split: ", split)
                #print("to float", float(split[1].replace(']', '')))
                if a % 500 == 0:
                    self.x.append(float(i[1]))
                    self.y.append(float(i[0]))
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
    path = 'results/01031221'
    path_2 = 'results/05126001'
    win = AnalysisPlot(path_2)

    
    sys.exit(app.exec_())
    
if __name__ == "__main__":
    main()