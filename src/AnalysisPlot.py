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
        self.pen2 = pg.mkPen(color=(255,0,255), width=5) # Style of the plot
        self.plot_psymex = pg.PlotWidget(title='Skin Conductance PsyMex') # Title
        self.plot_psymex.setAccessibleName('plot_gsr') # # Name property of plot_hr
        self.plot_psymex.setBackground('#212121') # Background color
        self.plot_psymex.setLabel('left', 'Micro  Siemens') # y axis label
        # Nexus Plot
        self.plot_nexus = pg.PlotWidget(title='Skin Conductance Nexus') # Title
        self.plot_nexus.setAccessibleName('plot_gsr') # # Name property of plot_hr
        self.plot_nexus.setBackground('#212121') # Background color
        self.plot_nexus.setLabel('left', 'Micro  Siemens') # y axis label
        # Plot property widget
        self.plot_prop = QWidget()
        self.variance = QWidget()
        self.mean = QWidget()
        self.stddev = QWidget()
        self.correlation = QWidget()
        self.legende = QWidget()
        
        # Statistics layout
        self.plot_prop_layout = QHBoxLayout()
        self.variance_layout = QVBoxLayout()
        self.mean_layout = QVBoxLayout()
        self.stddev_layout = QVBoxLayout()
        self.correlation_layout = QVBoxLayout()
        self.legende_layout = QVBoxLayout()
        
        # QLabel for statistics
        self.label_mean_psymex = QLabel()
        self.label_mean_psymex.setStyleSheet('color: #00D4DB; font: bold 20px')
        self.label_mean_nexus = QLabel()
        self.label_mean_nexus.setStyleSheet('color: #00D4DB; font: bold 20px')
        self.label_var_psymex = QLabel()
        self.label_var_psymex.setStyleSheet('color: #00D4DB; font: bold 20px')
        self.label_var_nexus = QLabel()
        self.label_var_nexus.setStyleSheet('color: #00D4DB; font: bold 20px')
        self.label_stddev_psymex = QLabel()
        self.label_stddev_psymex.setStyleSheet('color: #00D4DB; font: bold 20px')
        self.label_stddev_nexus = QLabel()
        self.label_stddev_nexus.setStyleSheet('color: #00D4DB; font: bold 20px')
        self.label_correlation = QLabel()
        self.label_correlation.setStyleSheet('color: #00D4DB; font: bold 20px')
        self.label_legende_p = QLabel("PsyMex = White")
        self.label_legende_p.setStyleSheet('color: #00D4DB; font: bold 20px')
        self.label_legende_n = QLabel("Nexus = Pink")
        self.label_legende_n.setStyleSheet('color: #00D4DB; font: bold 20px')
        
        self.mean_layout.addWidget(self.label_mean_psymex)
        self.mean_layout.addWidget(self.label_mean_nexus)
        self.variance_layout.addWidget(self.label_var_psymex)
        self.variance_layout.addWidget(self.label_var_nexus)
        self.stddev_layout.addWidget(self.label_stddev_psymex)
        self.stddev_layout.addWidget(self.label_stddev_nexus)
        self.correlation_layout.addWidget(self.label_correlation)
        self.legende_layout.addWidget(self.label_legende_p)
        self.legende_layout.addWidget(self.label_legende_n)

        self.variance.setLayout(self.variance_layout)
        self.mean.setLayout(self.mean_layout)
        self.stddev.setLayout(self.stddev_layout)
        self.plot_prop.setLayout(self.plot_prop_layout)
        self.correlation.setLayout(self.correlation_layout)
        self.legende.setLayout(self.legende_layout)
        
        self.plot_prop_layout.addWidget(self.mean)
        self.plot_prop_layout.addWidget(self.variance)
        self.plot_prop_layout.addWidget(self.stddev)
        self.plot_prop_layout.addWidget(self.correlation)
        self.plot_prop_layout.addWidget(self.legende)
        
        # Adding Widgets to overall layout
        self.layout.addWidget(self.plot_psymex)
        #self.layout.addWidget(self.plot_nexus)
        self.layout.addWidget(self.plot_prop)
        
        self.count()
        self.plot_psymex_data()
        self.plot_nexus_data()
        self.calc_correlation()
        
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
        
        with open(self.csv_psymex) as csv_file:
            c = csv.reader(csv_file, delimiter=',')
            for i in c:
                # starting at 3 seconds, every datapoint before is ignored
                if round(float(i[1]), 1) > 20:
                    
                    data_length += 1
                    val_sum_y += float(i[0]) * (10 ** 6)
                    x.append(float(i[1]))
                    y.append(float(i[0]) * (10 ** 6))
                    var.append(float(i[0]) * (10 ** 6))
        self.x_psymex = x
        self.y_psymex = y
        
        # normalize x values to fit in interval [0,1]
        count = 0
        min_x = min(x)
        max_x = max(x)
        for value in x:
            x[count] = (value - min_x) / (max_x - min_x)
            count += 1
        
        # Calculate mean
        mean = val_sum_y / data_length
        self.mean_psymex = mean
        # Calculate variance
        for v in var:
            var_sum += (v - mean) ** 2
        var = var_sum / data_length
        self.var_psymex = var
        # mean adjustment
        #count = 0
        #for value in y:
        #    y[count] = (value - mean)
        #    count += 1
        
        # z-transformation
        count = 0
        std_dev = math.sqrt(var)
        for value in y:
            y[count] = (value - mean) / std_dev
            count += 1
        
        self.plot_psymex.plot(x, y, pen=self.pen) # Symbol to use for data point
        
        self.label_mean_psymex.setText("Durchschnitt PsyMex: " + str(mean))
        self.label_var_psymex.setText("Varianz PsyMex: " + str(var))
        self.label_stddev_psymex.setText("Standardabweichung PsyMex: " + str(math.sqrt(var)))
        return
    
    def plot_nexus_data(self):
        '''
        This function plots the nexus data
        The nexus data is one large csv file therefore we need to split depending on the time stamp
        While iterating throug the data we calculate the mean
        lower and upper bound gives the interval where you want to observe the data
        nexus takes 32 datapoints each second so for example to start at 30 secons and end at 1:30
        lower_bound = 32 * 30
        upper_bound = 32 * 90
        '''
        x = []
        y = []
        var = [] # used to calculate variance
        var_sum = 0 # sum to calculate variance
        data_length = 0 # length of the data set, used for calculate the mean
        val_sum = 0 # sum of all y values, used to calculate the mean
        lower_bound = 32 * 2
        upper_bound = 32 * 30
        with open(self.csv_nexus) as csv_file:
            c = csv.reader(csv_file, delimiter=',')
            for i in c:
                if float(i[1]) > lower_bound:
                    data_length += 1
                    val_sum += float(i[0])
                    var.append(float(i[0]))
                    x.append(float(i[1]))
                    y.append(float(i[0]))
                    # Abortion condition if timestamp reached x
                    if float(i[1]) == upper_bound:
                        break
            self.x_nexus = x
            self.y_nexus = y
            
            # normalize x values to fit in interval [0,1]
            count = 0
            min_x = min(x)
            max_x = max(x)
            for value in x:
                x[count] = (value - min_x) / (max_x - min_x)
                count += 1
            
            # Calculate mean
            mean = val_sum / data_length
            self.mean_nexus = mean
            self.label_mean_nexus.setText("Durchschnitt Nexus: " + str(mean))
            
            # Calculate variance
            for v in var:
                var_sum += (v - mean) ** 2
            var = var_sum / data_length
            self.var_nexus = var
            
            # mean adjustment
            #count = 0
            #for value in y:
            #    y[count] = (value - mean)
            #    count += 1
            
            # z-transformation
            count = 0
            std_dev = math.sqrt(var)
            for value in y:
                y[count] = (value - mean) / std_dev
                count += 1
            
            self.label_var_nexus.setText("Varianz Nexus: " + str(var))
            self.label_stddev_nexus.setText("Standardabweichung Nexus: " + str(math.sqrt(var)))
            self.plot_psymex.plot(x, y, pen = self.pen2)
            return

    def calc_correlation(self):
        '''
        function to calculate correlation between psymex and nexus data
        '''
        s_1 = 0
        s_2 = 0
        s_3 = 0
        Y = []
        y_x = []
        sum_mean_y = 0
        sum_mean_x = 0
        if len(self.x_psymex) > len(self.x_nexus):
            up_x = self.x_psymex
            up_y = self.y_psymex
            low_x = self.x_nexus
            low_y = self.y_nexus
        else:
            up_x = self.x_nexus
            up_y = self.y_nexus
            low_x = self.x_psymex
            low_y = self.y_psymex
        
        for i in range(0, len(low_x)):
            x = low_x[i]
            y = up_x[i]
            c = 0
            while x > y:
                y = up_x[i + c]
                c += 1
            try:
                sum_mean_y += up_y[i+c]
                Y.append(up_y[i+c])
            except:
                sum_mean_y += up_y[i+c-1]
                Y.append(up_y[i+c-1])
            y_x.append(y)
            sum_mean_x += low_y[i]
            #print("x: ", y, "y: " , up_y[i+c])
            #print("x: ", x, "y: " , low_y[i])
        
        mean_Y = sum_mean_y / len(Y)
        mean_X = sum_mean_x / len(low_x)

        
        for i in range(0, len(low_x)):
            #print(low_y[i], " - ", mean_X, " * ", Y[i], " - ", mean_Y)
            s_1 += ((low_y[i] - mean_X) * (Y[i] - mean_Y))
            s_2 += ((low_y[i] - mean_X) ** 2)
            s_3 += ((Y[i] - mean_Y) ** 2)

        correlation =  s_1 / math.sqrt(( s_2 * s_3))
        self.label_correlation.setText("Korrelation: " + str(correlation))
        #self.plot_nexus.plot(low_y, Y, pen = self.pen, symbol='o')
        #self.plot_nexus.plot(Y, low_x, pen = self.pen, symbol='o')
        return
        
        
    def count(self):
        x = 0
        y = 0
        with open(self.csv_psymex) as csv_file:
            c = csv.reader(csv_file, delimiter=',')
            for i in c:
                x += 1
                if float(i[1]) > 1:
                    break
        return
    
def main():
    app = QApplication(sys.argv)
    path_nexus = "results/PilotStudie/Proband_6/23.04/two_hands/nexus"
    path_psymex = "results/PilotStudie/Proband_6/23.04/two_hands/psymex"
    win = AnalysisPlot(path_psymex, path_nexus)
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()