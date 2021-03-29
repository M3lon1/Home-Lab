import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import pyqtgraph as pg
from pulse.pulsesensor import Pulsesensor
from grove.grove_gsr_sensor import GroveGSRSensor

class MainWindow(QWidget):
    '''
    This is the main Window Class
    '''
    def __init__(self):
        '''
        Initializes MainWindow (PsyMexHub)
        
        '''
        super().__init__()
        self.setWindowTitle('PsyMex-2')
        self.setStyleSheet('QWidget { background-color: #212121; }')
        self.width = self.frameGeometry().width()
        self.height = self.frameGeometry().height()
        #-----------------------------------------------------------
        # Container (Group boxes) for Buttons
        self.container_left_menu = QGroupBox()
        self.container_left_menu.setStyleSheet('QGroupBox {background-color: #1c1c1c; margin-left: 0; margin-bottom: -0}')
        self.container_left_menu_layout = QVBoxLayout()
        self.container_left_menu.setLayout(self.container_left_menu_layout)
        
        self.container_right_hr_menu = QGroupBox()
        self.container_right_hr_menu.setStyleSheet('QGroupBox {}')
        self.container_right_hr_menu_layout = QVBoxLayout()
        self.container_right_hr_menu.setLayout(self.container_right_hr_menu_layout)
        
        self.container_right_gsr_menu = QGroupBox()
        self.container_right_gsr_menu.setStyleSheet('QGroupBox {}')
        self.container_right_gsr_menu_layout = QVBoxLayout()
        self.container_right_gsr_menu.setLayout(self.container_right_gsr_menu_layout)
        
        self.container_right_studies_list = QGroupBox()
        self.container_right_studies_list.setStyleSheet('QGroupBox {}')
        self.container_right_studies_list_layout = QVBoxLayout()
        self.container_right_studies_list.setLayout(self.container_right_studies_list_layout)
        
        #-----------------------------------------------------------
        # Buttons
            # Dashboard button
        button_home = QPushButton('Dashboard')
        button_home.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        button_home.setStyleSheet('''
        QPushButton {background-color: #1c1c1c; color: #82ECF0 ; border-style: outset; border-width: 0px; border-color: #1c1c1c; font: 20px}
        QPushButton:pressed {color: #82ECFF; font: bold 20px;}
        ''')
        button_home.clicked.connect(self.dashboard_button)
            
            # Heart Rate button
        button_hr = QPushButton('Heart Rate')
        button_hr.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        button_hr.setStyleSheet('''
        QPushButton {background-color: #1c1c1c; color: #82ECF0 ; border-style: outset; border-width: 0px; border-color: #1c1c1c; font: 20px}
        QPushButton:pressed {color: #82ECFF; font: bold 20px;}
        ''')
        button_hr.clicked.connect(self.hr_button)
            
            # Skin Conductance button
        button_gsr = QPushButton('Skin Conductance')
        button_gsr.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        button_gsr.setStyleSheet('''
        QPushButton {background-color: #1c1c1c; color: #82ECF0 ; border-style: outset; border-width: 0px; border-color: #1c1c1c; font: 20px}
        QPushButton:pressed {color: #82ECFF; font: bold 20px;}
        ''')
        button_gsr.clicked.connect(self.gsr_button)
        
                # Studies button
        button_studies = QPushButton('Studies')
        button_studies.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        button_studies.setStyleSheet('''
        QPushButton {background-color: #1c1c1c; color: #82ECF0 ; border-style: outset; border-width: 0px; border-color: #1c1c1c; font: 20px}
        QPushButton:pressed {color: #82ECFF; font: bold 20px;}
        ''')
        button_studies.clicked.connect(self.studies_button)
        
                # Piolt Studie button
        button_pilot_studies = QPushButton('Pilot Studie')
        button_pilot_studies.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        button_pilot_studies.setStyleSheet('''
        QPushButton {background-color: #1c1c1c; color: #82ECF0 ; border-style: outset; border-width: 0px; border-color: #1c1c1c; font: 20px}
        QPushButton:pressed {color: #82ECFF; font: bold 20px;}
        ''')
        button_pilot_studies.clicked.connect(self.start_pilot_studie)
        
        # Plot Buttons
        
        # Start Heart Rate Plot
        button_start_hr = QPushButton('Start')
        button_start_hr.setStyleSheet('''
        QPushButton {color: #82ECF0; border: none; font: 20px}
        QPushButton:pressed {color: #82ECFF; font: bold 20px;}
        ''')
        button_start_hr.clicked.connect(self.hr_plot)
        
        # Stop Heart Rate Plot
        button_stop_hr = QPushButton('Stop')
        button_stop_hr.setStyleSheet('''
        QPushButton {color: #82ECF0; border: none; font: 20px}
        QPushButton:pressed {color: #82ECFF; font: bold 20px;}
        ''')
        button_stop_hr.clicked.connect(self.hr_plot_stop)
        
        # Clear Hr Plot
        button_clear_hr = QPushButton('Clear')
        button_clear_hr.setStyleSheet('''
        QPushButton {color: #82ECF0; border: none; font: 20px}
        QPushButton:pressed {color: #82ECFF; font: bold 20px;}
        ''')
        button_clear_hr.clicked.connect(self.hr_plot_clear)
        
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
        
        # Adding Buttons to their Container
        self.container_left_menu_layout.addWidget(button_home)
        self.container_left_menu_layout.addWidget(button_hr)
        self.container_left_menu_layout.addWidget(button_gsr)
        self.container_left_menu_layout.addWidget(button_studies)
        
        self.container_right_hr_menu_layout.addWidget(button_start_hr)
        self.container_right_hr_menu_layout.addWidget(button_stop_hr)
        self.container_right_hr_menu_layout.addWidget(button_clear_hr)
        
        self.container_right_gsr_menu_layout.addWidget(button_start_gsr)
        self.container_right_gsr_menu_layout.addWidget(button_stop_gsr)
        self.container_right_gsr_menu_layout.addWidget(button_clear_gsr)
        
        self.container_right_studies_list_layout.addWidget(button_pilot_studies)
        #-----------------------------------------------------------
        # PsyMex-2 icon
        psymex_label = QLabel('<h1>PsyMex-2</h1>')
        psymex_label.setStyleSheet('color: #00D4DB; font: bold 20px')
        #-----------------------------------------------------------
        
        # Layouts
        self.layout_out = QHBoxLayout()
        self.layout_left = QVBoxLayout()
        self.layout_left_top = QVBoxLayout() # Psymex logo
        self.layout_left_bottom = QVBoxLayout() # Menu Bar
        self.layout_right = QVBoxLayout()
        self.layout_right_top = QHBoxLayout()
        self.layout_right_bottom = QHBoxLayout()
        self.layout_right_top_left = QVBoxLayout() # Heart Rate Buttons
        self.layout_right_top_right = QVBoxLayout() # Heart Rate Plot
        self.layout_right_bottom_left = QVBoxLayout() # GSR Buttons
        self.layout_right_bottom_right= QVBoxLayout() # GSR Plot
        
        # Psymex icon layout
        self.layout_left_top.setAlignment(Qt.AlignCenter)
        self.layout_left_top.setContentsMargins(5,5,5,5)
        self.layout_left_top.addWidget(psymex_label)
        
        # Menu Layout Vertical Box
        self.layout_left_bottom.setContentsMargins(0,5,5,0) # left top right bottom
        self.layout_left_bottom.addWidget(self.container_left_menu)
        
        # Heart Rate Buttons Layout
        self.layout_right_top_left.setContentsMargins(5,5,5,5)
        self.layout_right_top_left.addWidget(self.container_right_hr_menu)
        
        # GSR Buttons Layout
        self.layout_right_bottom_left.setContentsMargins(5,5,5,5)
        self.layout_right_bottom_left.addWidget(self.container_right_gsr_menu)
        
        # Building overal Layout
        self.layout_out.addLayout(self.layout_left, 1)
        self.layout_out.addLayout(self.layout_right, 6)
        self.layout_left.addLayout(self.layout_left_top, 1)
        self.layout_left.addLayout(self.layout_left_bottom, 3)
        self.layout_right.addLayout(self.layout_right_top, 1)
        self.layout_right.addLayout(self.layout_right_bottom, 1)
        self.layout_right_top.addLayout(self.layout_right_top_left)
        self.layout_right_top.addLayout(self.layout_right_top_right)
        self.layout_right_bottom.addLayout(self.layout_right_bottom_left)
        self.layout_right_bottom.addLayout(self.layout_right_bottom_right)
        self.setLayout(self.layout_out)
        #-----------------------------------------------------------
        # Live Plot
        self.pen = pg.mkPen(color=(255,255,255), width=2)
        self.plot_hr = pg.PlotWidget(title='Heart Rate')
        self.plot_hr.setAccessibleName('plot_hr')
        self.plot_hr.setBackground('#212121')
        self.plot_hr.setLabel('left', 'BPM')
        self.plot_hr.setLabel('bottom', 'Time (s)')
        self.plot_hr.setYRange(-10, 200)
        self.hr_line_ref = self.plot_hr.plot(pen=self.pen, symbol='o')
        self.layout_right_top_right.addWidget(self.plot_hr)
        
        self.plot_gsr = pg.PlotWidget(title='Skin Conductance')
        self.plot_gsr.setAccessibleName('plot_gsr')
        self.plot_gsr.setBackground('#212121')
        self.plot_gsr.setLabel('left', 'Micro  Siemens')
        self.plot_gsr.setLabel('bottom', 'Time (s)')
        self.plot_gsr.setYRange(-10,30)
        self.gsr_line_ref = self.plot_gsr.plot(pen=self.pen, symbol='o')
        self.layout_right_bottom_right.addWidget(self.plot_gsr)
        #-----------------------------------------------------------
        
        self.show()
    
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
    
    
    def hr_button(self):
        '''
        delete gsr section for dislaying heart rate only
        '''
        # Check if both views still exists then delete GSR
        if (self.layout_right_top_right.itemAt(0) and self.layout_right_top_left.itemAt(0) is not None) and (self.layout_right_bottom_right.itemAt(0) and self.layout_right_bottom_left.itemAt(0) is not None):
                    self.layout_right_bottom_right.itemAt(0).widget().setParent(None)
                    self.layout_right_bottom_left.itemAt(0).widget().setParent(None)
        # If GSR view exist but not HR
        if ((self.layout_right_top_right.itemAt(0) and self.layout_right_top_left.itemAt(0)) == None) and (self.layout_right_bottom_right.itemAt(0) and self.layout_right_bottom_left.itemAt(0) is not None):
                self.layout_right_bottom_right.itemAt(0).widget().setParent(None)
                self.layout_right_top_right.addWidget(self.plot_hr)
                self.layout_right_bottom_left.itemAt(0).widget().setParent(None)
                self.layout_right_top_left.addWidget(self.container_right_hr_menu)
        # Check if studies menu is shown
        if (self.layout_right_bottom_right.itemAt(0) and self.layout_right_bottom_right.itemAt(0).widget().accessibleName() != 'plot_gsr'):
            self.layout_right_bottom_right.itemAt(0).widget().setParent(None)
            self.layout_right_top_right.addWidget(self.plot_hr)
            self.layout_right_top_left.addWidget(self.container_right_hr_menu)
        else:
            pass
        return
    
    def gsr_button(self):
        '''
        delete gsr section for dislaying heart rate only
        '''
        # Check if both view still exists
        if (self.layout_right_top_right.itemAt(0) and self.layout_right_top_left.itemAt(0) is not None) and (self.layout_right_bottom_right.itemAt(0) and self.layout_right_bottom_left.itemAt(0) is not None):
            self.layout_right_top_right.itemAt(0).widget().setParent(None)
            self.layout_right_top_left.itemAt(0).widget().setParent(None)
        # If HR view exist but not GSR
        if (self.layout_right_bottom_right.itemAt(0) and self.layout_right_bottom_left.itemAt(0)) == None and (self.layout_right_top_right.itemAt(0) and self.layout_right_top_left.itemAt(0) is not None):
            self.layout_right_top_right.itemAt(0).widget().setParent(None)
            self.layout_right_bottom_right.addWidget(self.plot_gsr)
            self.layout_right_top_left.itemAt(0).widget().setParent(None)
            self.layout_right_bottom_left.addWidget(self.container_right_gsr_menu)
        # Check if studies menu is shown
        if (self.layout_right_bottom_right.itemAt(0) and self.layout_right_bottom_right.itemAt(0).widget().accessibleName() != 'plot_gsr'):
            self.layout_right_bottom_right.itemAt(0).widget().setParent(None)
            self.layout_right_bottom_right.addWidget(self.plot_gsr)
            self.layout_right_bottom_left.addWidget(self.container_right_gsr_menu)
        
        else:
            pass
        return
        
    def dashboard_button(self):
        '''
        todo: write generic version for adding/removing widgets/layouts
        Checks which layout is currently displayed 
        '''
        if self.layout_right_bottom_right.itemAt(0):
            if self.layout_right_bottom_right.itemAt(0).widget().accessibleName() != 'plot_gsr':
                self.layout_right_bottom_right.itemAt(0).widget().setParent(None)
        if self.layout_right_bottom_right.itemAt(0) is None:
            self.layout_right_bottom_right.addWidget(self.plot_gsr)
        if  self.layout_right_bottom_left.itemAt(0) is None:
            self.layout_right_bottom_left.addWidget(self.container_right_gsr_menu)
        if self.layout_right_top_right.itemAt(0) is None:
            self.layout_right_top_right.addWidget(self.plot_hr)
        if self.layout_right_top_left.itemAt(0) is None:
            self.layout_right_top_left.addWidget(self.container_right_hr_menu)
        return
    
    def studies_button(self):
        '''
        shows implemented studies
        '''
        # Check if both view still exists then clear all but right bottom corner
        if (self.layout_right_top_right.itemAt(0) and self.layout_right_top_left.itemAt(0) is not None) and (self.layout_right_bottom_right.itemAt(0) and self.layout_right_bottom_left.itemAt(0) is not None):
                self.layout_right_top_right.itemAt(0).widget().setParent(None)
                self.layout_right_top_left.itemAt(0).widget().setParent(None)
                self.layout_right_bottom_left.itemAt(0).widget().setParent(None)
                self.layout_right_bottom_right.itemAt(0).widget().setParent(None)
                self.layout_right_bottom_right.addWidget(self.container_right_studies_list)
        # If HR view exist but not GSR
        if (self.layout_right_bottom_right.itemAt(0) and self.layout_right_bottom_left.itemAt(0)) == None and (self.layout_right_top_right.itemAt(0) and self.layout_right_top_left.itemAt(0) is not None):
                self.layout_right_top_right.itemAt(0).widget().setParent(None)
                self.layout_right_bottom_right.addWidget(self.container_right_studies_list)
                self.layout_right_top_left.itemAt(0).widget().setParent(None)
        # If GSR view exist but not HR
        if ((self.layout_right_top_right.itemAt(0) and self.layout_right_top_left.itemAt(0)) == None) and (self.layout_right_bottom_right.itemAt(0) and self.layout_right_bottom_left.itemAt(0) is not None):
                self.layout_right_bottom_right.itemAt(0).widget().setParent(None)
                self.layout_right_bottom_right.addWidget(self.container_right_studies_list)
                self.layout_right_bottom_left.itemAt(0).widget().setParent(None)
                
    def start_pilot_studie(self):
        self.close()
        pass
        
def main():
    app = QApplication(sys.argv)
    GUI = MainWindow()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()