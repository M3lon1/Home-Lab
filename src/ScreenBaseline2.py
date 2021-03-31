import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from pulse.pulsesensor import Pulsesensor
from grove.grove_gsr_sensor import GroveGSRSensor
import time as t
import csv

class ScreenBaseline2(QMainWindow):
    def __init__(self, name, age, sex):
        super().__init__()
        self.name = name
        self.age = age
        self.sex = sex
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle("PsyMex-2 Pilot Studie Baseline")
        self.i = 0
        
        # Labels
        label_info_1 = QLabel("+")
        label_info_1.setStyleSheet('''
        QLabel {font: bold 50px; color: white}
        ''')
        label_info_1.setAlignment(Qt.AlignCenter)
        
        
        # Layout
        grid = QGridLayout()
        # Left/Right/Bottom layout just used for relative size of central box
        
        # Central box where the content is stored
        grid.addWidget(label_info_1,0,1,1,3)
        
        # Central Widget
        widget = QWidget()
        widget.setLayout(grid)
        widget.setStyleSheet('''
        QWidget {background-color: #1c1c1c}
        ''')
        self.setCentralWidget(widget)
        self.start_measurement()
        self.showMaximized()
        
    def next_page(self):
        pass

    def start_measurement(self):
        '''
        
        '''
        print("started")
        self.gsr_sensor = GroveGSRSensor()
        self.gsr_sensor.startAsyncGSR()
        self.pulse_sensor = Pulsesensor()
        self.pulse_sensor.startAsyncBPM()
        self.qt = QTimer()
        self.qt.timeout.connect(self.timer)
        self.qt.start(1000)
        return
    
    def timer(self):
        '''
        Wait for 30 seconds then save the sensor list to csv file
        '''
        print(self.i)
        self.i += 1
        if self.i == 3:
            print('saving')
            with open(self.name + str(self.age) + self.sex + "_gsr", 'w', newline='') as myfile:
                wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
                wr.writerow(self.gsr_sensor.GSR_list)
            with open(self.name + str(self.age) + self.sex + "_hr", 'w', newline='') as myfile:
                wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
                wr.writerow(self.pulse_sensor.BPM_list)
            self.gsr_sensor.stopAsyncGSR()
            self.qt.stop()
            return

def main():
    app = QApplication(sys.argv)
    info = ScreenBaseline2("Max Mustermann", 21, "Männlich")
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
