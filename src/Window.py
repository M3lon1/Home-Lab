import sys
from PyQt5.QtWidgets import *
#from PyQt5.QtGui import *
from PyQt5.QtCore import *
from matplotlib.backends.backend_qt5agg import FigureCanvas
import matplotlib as mpl
import matplotlib.figure as mpl_fig
import matplotlib.animation as anim
import numpy as np
import random as rnd
from graph import *
import pyqtgraph as pg
from pulse.pulsesensor import Pulsesensor
from grove.grove_gsr_sensor import GroveGSRSensor
import datetime

class Window(QWidget):
    '''
    This is the main Window Class
    '''
    def __init__(self):
        super().__init__()
        self.setWindowTitle('PsyMex-2')
        self.setStyleSheet('QWidget { background-color: #212121; }')
        self.width = self.frameGeometry().width()
        self.height = self.frameGeometry().height()
        
        # Dashboard button
        button_home = QPushButton('Dashboard')
        button_home.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        button_home.setStyleSheet('''
        QPushButton {color: #82ECF0; border: none; font: 20px}
        QPushButton:pressed {color: #82ECFF; font: bold 20px;}
        ''') # Border needs to be set to none to change background
        #button_home.setStyleSheet('QPushButton:pressed {border-style: outset; border-width: 2px; border-radius: 10px; border-color: #424242; font: bold 20px }')
        # Heart Rate button
        button_hr = QPushButton('Heart Rate')
        button_hr.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        button_hr.setStyleSheet('''
        QPushButton {color: #82ECF0; border: none; font: 20px}
        QPushButton:pressed {color: #82ECFF; font: bold 20px;}
        ''')
        # Heart Rate button
        button_gsr = QPushButton('Skin Conductance')
        button_gsr.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        button_gsr.setStyleSheet('''
        QPushButton {color: #82ECF0; border: none; font: 20px}
        QPushButton:pressed {color: #82ECFF; font: bold 20px;}
        ''')
        
        # PsyMex-2 icon
        psymex_label = QLabel('<h1>PsyMex-2</h1>')
        psymex_label.setStyleSheet('color: #00D4DB; font: bold 20px')
        
        # Layouts
        outer_layout = QHBoxLayout()
        left_bar = QVBoxLayout()
        
        # Psymex icon layout
        psymex_layout = QVBoxLayout()
        psymex_layout.setAlignment(Qt.AlignCenter)
        psymex_layout.setContentsMargins(5,5,5,5)
        psymex_layout.addWidget(psymex_label)
        
        # Menu Layout Vertical Box
        menu_layout = QVBoxLayout()
        menu_layout.setSpacing(5)
        menu_layout.setContentsMargins(5,5,5,5) # left top right bottom
        menu_layout.addWidget(button_home, 1)
        menu_layout.addWidget(button_hr, 1)
        menu_layout.addWidget(button_gsr, 1)
        
        # Live Plot
        self.pen = pg.mkPen(color=(255,255,255), width=2)
        
        view = QVBoxLayout()
        self.plot_hr = pg.PlotWidget(title='Heart Rate')
        self.plot_hr.setBackground('#212121')
        self.plot_hr.setLabel('left', 'BPM')
        self.plot_hr.setLabel('bottom', 'Time (s)')
        #self.plot_hr.setXRange(0,20)
        self.plot_hr.setYRange(30,150)
        self.line_ref = self.plot_hr.plot(pen=self.pen, symbol='o')
        view.addWidget(self.plot_hr)
        self.hr_plot()
        
        self.plot_gsr = pg.PlotWidget(title='Skin Conductance')
        self.plot_gsr.setBackground('#212121')
        view.addWidget(self.plot_gsr)
        
        # Building overal Layout
        left_bar.addLayout(psymex_layout, 1)
        left_bar.addLayout(menu_layout, 2)
        outer_layout.addLayout(left_bar,1)
        outer_layout.addLayout(view, 4)
        
        self.setLayout(outer_layout)
    
    def hr_plot(self):
        '''
        QTimer gets called every interval
        '''
        self.hr_x = [0]
        self.hr_y = [0]
        self.pulse_sensor = Pulsesensor()
        self.pulse_sensor.startAsyncBPM()
        self.hr_timer = QtCore.QTimer()
        self.hr_timer.timeout.connect(self.update_plot)
        self.hr_timer.start(500)
        
    
    def update_plot(self):
        if len(self.pulse_sensor.BPM_list) > 1:
            if self.hr_y[-1] != self.pulse_sensor.BPM_list[-1][0]:
                self.hr_x.append(int(self.pulse_sensor.BPM_list[-1][1]))
                self.hr_y.append(self.pulse_sensor.BPM_list[-1][0])

        try:
            self.line_ref.setData(self.hr_x, self.hr_y)
            print(self.hr_x, self.hr_y)
            print(len(self.pulse_sensor.BPM_list))
            print("update_plot")
        except:
            print(len(self.pulse_sensor.BPM_list))
            print(sys.exc_info())
    
            
def main():
    app = QApplication(sys.argv)
    GUI = Window()
    GUI.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()