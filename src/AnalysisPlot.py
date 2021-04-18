import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import pyqtgraph as pg
from pulse.pulsesensor import Pulsesensor
from grove.grove_gsr_sensor import GroveGSRSensor
from PilotStudie import *
import csv
import numpy as np
import math

class AnalysisPlot(QMainWindow):
    def __init__(self, csv_psymex, csv_nexus):
        """
        this class plots a csv file
        """
        super().__init__()
        self.csv_psymex = csv_psymex
        self.csv_nexus = csv_nexus
        self.layout = QVBoxLayout()
        # PsyMex Plot 
        self.pen = pg.mkPen(color=(255,255,255), width=2) # Style of the plot
        self.plot_psymex = pg.PlotWidget(title='Skin Conductance') # Title
        self.plot_psymex.setAccessibleName('plot_gsr') # # Name property of plot_hr
        self.plot_psymex.setBackground('#212121') # Background color
        self.plot_psymex.setLabel('left', 'Micro  Siemens') # y axis label
        # Nexus Plot
        self.plot_nexus = pg.PlotWidget(title='Skin Conductance') # Title
        self.plot_nexus.setAccessibleName('plot_gsr') # # Name property of plot_hr
        self.plot_nexus.setBackground('#212121') # Background color
        self.plot_nexus.setLabel('left', 'Micro  Siemens') # y axis label
        # Plot property widget
        self.plot_prop = QWidget()
        self.variance = QWidget()
        self.mean = QWidget()
        self.stddev = QWidget()
        
        # Statistics layout
        self.plot_prop_layout = QHBoxLayout()
        self.variance_layout = QVBoxLayout()
        self.mean_layout = QVBoxLayout()
        self.stddev_layout = QVBoxLayout()
        
        # QLabel for statistics
        self.mean_psymex = QLabel()
        self.mean_psymex.setStyleSheet('color: #00D4DB; font: bold 20px')
        self.mean_nexus = QLabel()
        self.mean_nexus.setStyleSheet('color: #00D4DB; font: bold 20px')
        self.var_psymex = QLabel()
        self.var_psymex.setStyleSheet('color: #00D4DB; font: bold 20px')
        self.var_nexus = QLabel()
        self.var_nexus.setStyleSheet('color: #00D4DB; font: bold 20px')
        self.stddev_psymex = QLabel()
        self.stddev_psymex.setStyleSheet('color: #00D4DB; font: bold 20px')
        self.stddev_nexus = QLabel()
        self.stddev_nexus.setStyleSheet('color: #00D4DB; font: bold 20px')
        
        self.mean_layout.addWidget(self.mean_psymex)
        self.mean_layout.addWidget(self.mean_nexus)
        self.variance_layout.addWidget(self.var_psymex)
        self.variance_layout.addWidget(self.var_nexus)
        self.stddev_layout.addWidget(self.stddev_psymex)
        self.stddev_layout.addWidget(self.stddev_nexus)
        
        self.plot_prop_layout.addWidget(self.mean)
        self.plot_prop_layout.addWidget(self.variance)
        self.plot_prop_layout.addWidget(self.stddev)
        
        
        self.variance.setLayout(self.variance_layout)
        self.mean.setLayout(self.mean_layout)
        self.stddev.setLayout(self.stddev_layout)
        self.plot_prop.setLayout(self.plot_prop_layout)
        
        
        
        
        # Adding Widgets to overall layout
        self.layout.addWidget(self.plot_psymex)
        self.layout.addWidget(self.plot_nexus)
        self.layout.addWidget(self.plot_prop)
        
        self.plot_psymex_data()
        self.plot_nexus_data()
        
        widget = QWidget()
        widget.setLayout(self.layout)
        widget.setStyleSheet('''
        QWidget {background-color: #1c1c1c}
        ''')
        self.setCentralWidget(widget)
        self.showMaximized()
        
    def plot_psymex_data(self):
        '''
        This function plots the psymex data
        The psymex data is split up into separate files for each task
        While iterating throug the data we calculate the mean
        '''
        x = []
        y = []
        var = [] # used to calculate variance
        var_sum = 0 # sum to calculate variance
        data_length = 0 # length of the data set, used for calculate the mean
        val_sum_y = 0 # sum of all y values, used to calculate the mean
        val_sum_x = 0
        with open(self.csv_psymex) as csv_file:
            c = csv.reader(csv_file, delimiter=',')
            # Loop through every line
            for i in c:
                data_length += 1
                val_sum_y += float(i[0]) * (10 ** 6)
                # starting at 3 seconds 
                if round(float(i[1]), 1) > 2:
                    x.append(float(i[1]))
                    y.append(float(i[0]) * (10 ** 6))
                    var.append(float(i[0]) * (10 ** 6))
        mean_y = val_sum_y / data_length
        
        
        # Calculate variance
        for v in var:
            var_sum += (v - mean_y) ** 2
        var = var_sum / data_length
        
        # mean adjustment
        #count = 0
        #for j in x:
        #    y[count] = (j - mean_y) / math.sqrt(var)
        #    count += 1
        
        self.plot_psymex.plot(x, y, pen=self.pen, symbol='o') # Symbol to use for data point

        print("PsyMex datalength: ", data_length)
        
        self.mean_psymex.setText("Durchschnitt PsyMex: " + str(mean_y))
        self.var_psymex.setText("Varianz PsyMex: " + str(var))
        self.stddev_psymex.setText("Standardabweichung PsyMex: " + str(math.sqrt(var)))
        return
    
    def plot_nexus_data(self):
        '''
        This function plots the nexus data
        The nexus data is one large csv file therefore we need to split depending on the time stamp
        While iterating throug the data we calculate the mean
        '''
        x = []
        y = []
        var = [] # used to calculate variance
        var_sum = 0 # sum to calculate variance
        data_length = 0 # length of the data set, used for calculate the mean
        val_sum = 0 # sum of all y values, used to calculate the mean
        with open(self.csv_nexus) as csv_file:
            c = csv.reader(csv_file, delimiter=',')
            for i in c:
                # Nexus takes 32 samples per second
                if float(i[1]) > 64:
                    data_length += 1
                    val_sum += float(i[0])
                    var.append(float(i[0]))
                    x.append(float(i[1]))
                    y.append(float(i[0]))
                # Abortion condition if timestamp reached x seconds
                if float(i[1]) == 960:
                    mean = val_sum / data_length
                    self.mean_nexus.setText("Durchschnitt Nexus: " + str(mean))
                            # Calculate variance
                    for v in var:
                        var_sum += (v - mean) ** 2
                    var = var_sum / data_length
                    self.var_nexus.setText("Varianz Nexus: " + str(var))
                    self.stddev_nexus.setText("Standardabweichung Nexus: " + str(math.sqrt(var)))
                    self.plot_nexus.plot(x, y, pen = self.pen, symbol='o')
                    print("Nexus datalength: ", data_length)
                    return
        
        def calc_correlation(self):
            pass
                    
def main():
    app = QApplication(sys.argv)
    win = AnalysisPlot('results/Rebecca/04224001', "results/Rebecca/result_nexus_csv_adjusted")
    sys.exit(app.exec_())
    
if __name__ == "__main__":
    main()