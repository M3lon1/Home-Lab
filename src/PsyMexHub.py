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

class MainWindow(QWidget):
    '''
    This is the main Window Class
    '''
    def __init__(self):
        super().__init__()
        self.setWindowTitle('PsyMex-2')
        self.setStyleSheet('QWidget { background-color: #212121; }')
        self.width = self.frameGeometry().width()
        self.height = self.frameGeometry().height()
        #-----------------------------------------------------------
        # Container (Group boxes) for Buttons
        container_left_menu = QGroupBox()
        container_left_menu.setStyleSheet('QGroup {}')
        container_left_menu_layout = QVBoxLayout()
        container_left_menu.setLayout(container_left_menu_layout)
        
        container_right_hr_menu = QGroupBox()
        container_right_hr_menu.setStyleSheet('QGroup {}')
        container_right_hr_menu_layout = QVBoxLayout()
        container_right_hr_menu.setLayout(container_right_hr_menu_layout)
        
        container_right_gsr_menu = QGroupBox()
        container_right_gsr_menu.setStyleSheet('QGroup {}')
        container_right_gsr_menu_layout = QVBoxLayout()
        container_right_gsr_menu.setLayout(container_right_gsr_menu_layout)
        #-----------------------------------------------------------
        # Buttons
            # Dashboard button
        button_home = QPushButton('Dashboard')
        button_home.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        button_home.setStyleSheet('''
        QPushButton {color: #82ECF0; border: none; font: 20px}
        QPushButton:pressed {color: #82ECFF; font: bold 20px;}
        ''') # Border needs to be set to none to change background
        
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
        
        # Plot Buttons
        # Start Heart Rate Plot
        self.button_start_hr = QPushButton('Start')
        self.button_start_hr.setStyleSheet('''
        QPushButton {color: #82ECF0; border: none; font: 20px}
        QPushButton:pressed {color: #82ECFF; font: bold 20px;}
        ''')
        self.button_start_hr.clicked.connect(self.hr_plot)
        # Stop Heart Rate Plot
        self.button_stop_hr = QPushButton('Stop')
        self.button_stop_hr.setStyleSheet('''
        QPushButton {color: #82ECF0; border: none; font: 20px}
        QPushButton:pressed {color: #82ECFF; font: bold 20px;}
        ''')
        self.button_stop_hr.clicked.connect(self.hr_plot_stop)
        
        # Start GSR Plot
        self.button_start_gsr = QPushButton('Start')
        self.button_start_gsr.setStyleSheet('''
        QPushButton {color: #82ECF0; border: none; font: 20px}
        QPushButton:pressed {color: #82ECFF; font: bold 20px;}
        ''')
        self.button_start_gsr.clicked.connect(self.gsr_plot)
        # Stop GSR Plot
        self.button_stop_gsr = QPushButton('Stop')
        self.button_stop_gsr.setStyleSheet('''
        QPushButton {color: #82ECF0; border: none; font: 20px}
        QPushButton:pressed {color: #82ECFF; font: bold 20px;}
        ''')
        self.button_stop_gsr.clicked.connect(self.gsr_plot_stop)
        
        # Adding Buttons to their Container
        container_left_menu_layout.addWidget(button_home)
        container_left_menu_layout.addWidget(button_hr)
        container_left_menu_layout.addWidget(button_gsr)
        
        container_right_hr_menu_layout.addWidget(self.button_start_hr)
        container_right_hr_menu_layout.addWidget(self.button_stop_hr)
        
        container_right_gsr_menu_layout.addWidget(self.button_start_gsr)
        container_right_gsr_menu_layout.addWidget(self.button_stop_gsr)
        #-----------------------------------------------------------
        # PsyMex-2 icon
        psymex_label = QLabel('<h1>PsyMex-2</h1>')
        psymex_label.setStyleSheet('color: #00D4DB; font: bold 20px')
        #-----------------------------------------------------------
        # Layouts
        layout_out = QHBoxLayout()
        layout_left = QVBoxLayout()
        layout_left_top = QVBoxLayout() # Psymex logo
        layout_left_bottom = QVBoxLayout() # Menu Bar
        layout_right = QVBoxLayout()
        layout_right_top = QHBoxLayout()
        layout_right_bottom = QHBoxLayout()
        layout_right_top_left = QVBoxLayout() # Heart Rate Buttons
        layout_right_top_right = QVBoxLayout() # Heart Rate Plot
        layout_right_bottom_left = QVBoxLayout() # GSR Buttons
        layout_right_bottom_right= QVBoxLayout() # GSR Plot
        
        # Psymex icon layout
        layout_left_top.setAlignment(Qt.AlignCenter)
        layout_left_top.setContentsMargins(5,5,5,5)
        layout_left_top.addWidget(psymex_label)
        
        # Menu Layout Vertical Box
        layout_left_bottom.setContentsMargins(5,5,5,5) # left top right bottom
        layout_left_bottom.addWidget(container_left_menu)
        
        # Heart Rate Buttons Layout
        layout_right_top_left.setContentsMargins(5,5,5,5)
        layout_right_top_left.addWidget(container_right_hr_menu)
        
        # GSR Buttons Layout
        layout_right_bottom_left.setContentsMargins(5,5,5,5)
        layout_right_bottom_left.addWidget(container_right_gsr_menu)
        # Building overal Layout
        layout_out.addLayout(layout_left, 1)
        layout_out.addLayout(layout_right, 4)
        
        layout_left.addLayout(layout_left_top)
        layout_left.addLayout(layout_left_bottom)
    
        layout_right.addLayout(layout_right_top)
        layout_right.addLayout(layout_right_bottom)
        layout_right_top.addLayout(layout_right_top_left)
        layout_right_top.addLayout(layout_right_top_right)
        layout_right_bottom.addLayout(layout_right_bottom_left)
        layout_right_bottom.addLayout(layout_right_bottom_right)
        #-----------------------------------------------------------
        # Live Plot
        self.pen = pg.mkPen(color=(255,255,255), width=2)
        self.plot_hr = pg.PlotWidget(title='Heart Rate')
        self.plot_hr.setBackground('#212121')
        self.plot_hr.setLabel('left', 'BPM')
        self.plot_hr.setLabel('bottom', 'Time (s)')
        self.plot_hr.setYRange(30,150)
        self.hr_line_ref = self.plot_hr.plot(pen=self.pen, symbol='o')
        layout_right_top_right.addWidget(self.plot_hr)
        
        self.plot_gsr = pg.PlotWidget(title='Skin Conductance')
        self.plot_gsr.setBackground('#212121')
        self.plot_gsr.setLabel('left', 'Siemens')
        self.plot_gsr.setLabel('bottom', 'Time (s)')
        self.plot_hr.setYRange(-10,100)
        self.gsr_line_ref = self.plot_gsr.plot(pen=self.pen, symbol='o')
        layout_right_bottom_right.addWidget(self.plot_gsr)
        #-----------------------------------------------------------
        
        
        '''
        left_bar.addLayout(psymex_layout, 1)
        left_bar.addLayout(menu_layout, 2)
        outer_layout.addLayout(left_bar,1)
        outer_layout.addLayout(view_layout, 4)
        view_layout.addLayout(view_buttons_layout, 1)
        '''
        self.setLayout(layout_out)
    
    
    def hr_plot(self):
        '''
        QTimer gets called every interval
        '''
        self.check_hr_plot = True
        self.hr_x = [0]
        self.hr_y = [0]
        self.pulse_sensor = Pulsesensor()
        self.pulse_sensor.startAsyncBPM()
        self.hr_timer = QtCore.QTimer()
        self.hr_timer.timeout.connect(self.update_hr_plot)
        self.hr_timer.start(500)
        return
    
    def hr_plot_stop(self):
        self.check_hr_plot = False
        return

    def update_hr_plot(self):
        if self.check_hr_plot:
            if len(self.pulse_sensor.BPM_list) > 1:
                if self.hr_y[-1] != self.pulse_sensor.BPM_list[-1][0]:
                    self.hr_x.append(int(self.pulse_sensor.BPM_list[-1][1]))
                    self.hr_y.append(self.pulse_sensor.BPM_list[-1][0])
            try:
                self.hr_line_ref.setData(self.hr_x, self.hr_y)
                print(self.hr_x, self.hr_y)
                print(len(self.pulse_sensor.BPM_list))
                print("update_plot")
            except:
                print(sys.exc_info())
        else:
            self.pulse_sensor.stopAsyncBPM()
            
    def gsr_plot(self):
        self.check_gsr_plot = True
        self.gsr_x = [0]
        self.gsr_y = [0]
        self.gsr_sensor = GroveGSRSensor()
        self.gsr_sensor.startAsyncGSR()
        self.gsr_timer = QtCore.QTimer()
        self.gsr_timer.timeout.connect(self.update_gsr_plot)
        self.gsr_timer.start(500)
        return
    
    def gsr_plot_stop(self):
        self.check_gsr_plot = False
        return
    
    def update_gsr_plot(self):
        if self.check_gsr_plot:
            if len(self.gsr_sensor.GSR_list) > 1:
                if self.gsr_y[-1] != self.gsr_sensor.GSR_list[-1][0]:
                    y = self.gsr_sensor.GSR_list[-1][0] * 10**6
                    print(y)
                    self.gsr_y.append(y)
                    self.gsr_x.append(self.gsr_sensor.GSR_list[-1][1])
            try:
                self.gsr_line_ref.setData(self.gsr_x, self.gsr_y)
            except:
                print(sys.exc_info())
        else:
            self.gsr_sensor.stopAsyncGSR()
        
def main():
    app = QApplication(sys.argv)
    GUI = MainWindow()
    GUI.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()