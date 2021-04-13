import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import QIcon, QPixmap
import pyqtgraph as pg
from pulse.pulsesensor import Pulsesensor
from grove.grove_gsr_sensor import GroveGSRSensor
from ScreenSensorsHR import *

class ScreenSensorsGSR(QMainWindow):
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
        
        
        label_gsr_pic = QLabel()
        pixmap = QPixmap('pic/Instructions/DSC03715.JPG')
        
        label_gsr_pic.setPixmap(pixmap)
        label_gsr_pic.setAlignment(Qt.AlignCenter)
        label_gsr_pic.setScaledContents(1)
        
        container = QWidget()
        container.setMaximumSize(587,470)
        container.setMinimumSize(0,0)
        
        container_layout = QHBoxLayout(container)
        container_layout.addWidget(label_gsr_pic)
        
        # Next button
        next_button = QPushButton("Weiter")
        next_button.setStyleSheet('''
        QPushButton {margin: 20 200 50 200}
        ''')
        next_button.clicked.connect(self.next_page)
        
        # Start GSR Plot
        button_start_gsr = QPushButton('Start')
        button_start_gsr.setStyleSheet('''
        QPushButton {color: #82ECF0; border: none; font: 20px}
        QPushButton:pressed {color: #82ECFF; font: bold 20px;}
        ''')
        button_start_gsr.clicked.connect(self.gsr_plot)
        # Stop GSR Plot
        button_stop_gsr = QPushButton('Stop')
        button_stop_gsr.setStyleSheet('''
        QPushButton {color: #82ECF0; border: none; font: 20px}
        QPushButton:pressed {color: #82ECFF; font: bold 20px;}
        ''')
        button_stop_gsr.clicked.connect(self.gsr_plot_stop)
        # Clear GSR Plot
        button_clear_gsr = QPushButton('Clear')
        button_clear_gsr.setStyleSheet('''
        QPushButton {color: #82ECF0; border: none; font: 20px}
        QPushButton:pressed {color: #82ECFF; font: bold 20px;}
        ''')
        button_clear_gsr.clicked.connect(self.gsr_plot_clear)
        
        # container for gsr start stop clear buttons
        con = QGroupBox()
        con.setStyleSheet('QGroupBox {}')
        con_layout = QHBoxLayout()
        con.setLayout(con_layout)
        
        con_layout.addWidget(button_start_gsr)
        con_layout.addWidget(button_stop_gsr)
        con_layout.addWidget(button_clear_gsr)
        
        # Live Plot for testing
        self.pen = pg.mkPen(color=(255,255,255), width=2)
        self.plot_gsr = pg.PlotWidget(title='Skin Conductance')
        self.plot_gsr.setAccessibleName('plot_gsr')
        self.plot_gsr.setBackground('#212121')
        self.plot_gsr.setLabel('left', 'Micro  Siemens')
        self.plot_gsr.setLabel('bottom', 'Time (s)')
        self.plot_gsr.setYRange(-10,30)
        self.gsr_line_ref = self.plot_gsr.plot(pen=self.pen, symbol='o')
        
        # Layout
        grid = QGridLayout()
        # Left/Right/Bottom layout just used for relative size of central box
        
        # Central box where the content is stored
        grid.addWidget(label_info_1,0,1,1,3)
        grid.addWidget(container,1,1,1,1)
        grid.addWidget(self.plot_gsr,1,2,1,1)
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
        self.next_page = ScreenSensorsHR(self.name, self.identifier)
        self.close()
        
    def gsr_plot(self):
        self.check_gsr_plot = True
        self.gsr_x = [0]
        self.gsr_y = [0]
        self.gsr_sensor = GroveGSRSensor()
        self.gsr_sensor.startAsyncGSR()
        self.gsr_timer = QTimer()
        self.gsr_timer.timeout.connect(self.update_gsr_plot)
        self.gsr_timer.start(500)
        return
    
    def gsr_plot_stop(self):
        self.gsr_timer.stop()
        self.gsr_sensor.stopAsyncGSR()
        return
    
    def gsr_plot_clear(self):
        plt = self.plot_gsr.getPlotItem()
        plt.clear()
        self.gsr_line_ref = self.plot_gsr.plot(pen=self.pen, symbol='o')
        return
    
    def update_gsr_plot(self):
        if len(self.gsr_sensor.GSR_list) > 1:
            if self.gsr_y[-1] != self.gsr_sensor.GSR_list[-1][0]:
                y = self.gsr_sensor.GSR_list[-1][0] * 10**6
                self.gsr_y.append(y)
                self.gsr_x.append(self.gsr_sensor.GSR_list[-1][1])
        try:
            self.gsr_line_ref.setData(self.gsr_x, self.gsr_y)
        except:
            print(sys.exc_info())

def main():
    app = QApplication(sys.argv)
    info = ScreenSensorsGSR("Max Mustermann", "1234556")
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()

