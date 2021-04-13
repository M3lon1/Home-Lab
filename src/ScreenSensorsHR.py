import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import QIcon, QPixmap
import pyqtgraph as pg
from pulse.pulsesensor import Pulsesensor
from grove.grove_gsr_sensor import GroveGSRSensor
from ScreenInstructions import *

class ScreenSensorsHR(QMainWindow):
    def __init__(self, name, identifier):
        super().__init__()
        self.name = name
        self.identifier = identifier
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle("PsyMex-2 Pilot Studie Instructuions")
        
        
        # Labels
        label_info_1 = QLabel("Bitte bringe nun die Sensoren an und teste sie mit dem rechten Live Diagram")
        label_info_1.setStyleSheet('''
        QLabel {font: bold 30px; color: white}
        ''')
        label_info_1.setAlignment(Qt.AlignCenter)
        
        
        label_hr_pic = QLabel()
        pixmap = QPixmap('pic/Instructions/DSC03717.JPG')
        label_hr_pic.setPixmap(pixmap)
        label_hr_pic.setAlignment(Qt.AlignCenter)
        label_hr_pic.setScaledContents(1)
        
        container = QWidget()
        container.setMaximumSize(587,470)
        container.setMinimumSize(0,0)
        
        container_layout = QHBoxLayout(container)
        container_layout.addWidget(label_hr_pic)
        
        # Next button
        next_button = QPushButton("Weiter")
        next_button.setStyleSheet('''
        QPushButton {margin: 20 200 50 200}
        ''')
        next_button.clicked.connect(self.next_page)
        
        # Start GSR Plot
        button_start_hr = QPushButton('Start')
        button_start_hr.setStyleSheet('''
        QPushButton {color: #82ECF0; border: none; font: 20px}
        QPushButton:pressed {color: #82ECFF; font: bold 20px;}
        ''')
        button_start_hr.clicked.connect(self.hr_plot)
        # Stop GSR Plot
        button_stop_hr = QPushButton('Stop')
        button_stop_hr.setStyleSheet('''
        QPushButton {color: #82ECF0; border: none; font: 20px}
        QPushButton:pressed {color: #82ECFF; font: bold 20px;}
        ''')
        button_stop_hr.clicked.connect(self.hr_plot_stop)
        # Clear GSR Plot
        button_clear_hr = QPushButton('Clear')
        button_clear_hr.setStyleSheet('''
        QPushButton {color: #82ECF0; border: none; font: 20px}
        QPushButton:pressed {color: #82ECFF; font: bold 20px;}
        ''')
        button_clear_hr.clicked.connect(self.hr_plot_clear)
        
        # container for gsr start stop clear buttons
        con = QGroupBox()
        con.setStyleSheet('QGroupBox {}')
        con_layout = QHBoxLayout()
        con.setLayout(con_layout)
        
        con_layout.addWidget(button_start_hr)
        con_layout.addWidget(button_stop_hr)
        con_layout.addWidget(button_clear_hr)
        
        # Live Plot for testing
        self.pen = pg.mkPen(color=(255,255,255), width=2)
        self.plot_hr = pg.PlotWidget(title='Heart Rate')
        self.plot_hr.setAccessibleName('plot_hr')
        self.plot_hr.setBackground('#212121')
        self.plot_hr.setLabel('left', 'BPM')
        self.plot_hr.setLabel('bottom', 'Time (s)')
        self.plot_hr.setYRange(-10, 200)
        self.hr_line_ref = self.plot_hr.plot(pen=self.pen, symbol='o')
        
        # Layout
        grid = QGridLayout()
        # Left/Right/Bottom layout just used for relative size of central box
        
        # Central box where the content is stored
        grid.addWidget(label_info_1,0,1,1,3)
        grid.addWidget(container,1,1,1,1)
        grid.addWidget(self.plot_hr,1,2,1,1)
        grid.addWidget(con, 3,2,1,1)
        grid.addWidget(next_button,6,2,5,1)
        
    
        # Central Widget
        widget = QWidget()
        widget.setLayout(grid)
        widget.setStyleSheet('''
        QWidget {background-color: #1c1c1c}
        ''')
        self.setCentralWidget(widget)
        self.showMaximized()
    
    def next_page(self):
        self.next_page = ScreenInstructions(self.name, self.identifier)
        self.close()
        
    def hr_plot(self):
        '''
        QTimer gets called every interval
        '''
        self.check_hr_plot = True
        self.hr_x = [0]
        self.hr_y = [0]
        self.pulse_sensor = Pulsesensor()
        self.pulse_sensor.startAsyncBPM()
        self.hr_timer = QTimer()
        self.hr_timer.timeout.connect(self.update_hr_plot)
        self.hr_timer.start(500)
        return
    
    def hr_plot_stop(self):
        self.hr_timer.stop()
        self.pulse_sensor.stopAsyncBPM()
        return
    
    def hr_plot_clear(self):
        plt = self.plot_hr.getPlotItem()
        plt.clear()
        self.hr_line_ref = self.plot_hr.plot(pen=self.pen, symbol='o')

    def update_hr_plot(self):
        if len(self.pulse_sensor.BPM_list) > 1:
            if self.hr_y[-1] != self.pulse_sensor.BPM_list[-1][0]:
                self.hr_x.append(int(self.pulse_sensor.BPM_list[-1][1]))
                self.hr_y.append(self.pulse_sensor.BPM_list[-1][0])
        try:
            self.hr_line_ref.setData(self.hr_x, self.hr_y)
        except:
            print(sys.exc_info())

def main():
    app = QApplication(sys.argv)
    info = ScreenSensorsHR("Max Mustermann", "1234556")
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()


