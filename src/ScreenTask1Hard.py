import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from pulse.pulsesensor import Pulsesensor
from grove.grove_gsr_sensor import GroveGSRSensor
from PyQt5.QtGui import *
from ScreenInstructions2 import *

class ScreenTask1Hard(QMainWindow):
    def __init__(self, name, identifier):
        super().__init__()
        self.name = name
        self.identifier = identifier
        self.nr = "12"
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle("PsyMex-2 Pilot Aufgabe 1 leicht")
        self.i = 0 
        
        # Labels
        self.label_info_1 = QLabel("Aufgabe 1 Schwer")
        self.label_info_1.setStyleSheet('''
        QLabel {font: bold 30px; color: white}
        ''')
        self.label_info_1.setAlignment(Qt.AlignCenter)
        
        self.label_info_2 = QLabel("Subtrahiere die Zahl 17 immer weiter bis die Zeit vorbei ist")
        self.label_info_2.setStyleSheet('''
        QLabel {font: bold 30px; color: white}
        ''')
        self.label_info_2.setAlignment(Qt.AlignCenter)
        
        self.label_info_3 = QLabel("Beginne bei der Zahl 7561")
        self.label_info_3.setStyleSheet('''
        QLabel {font: bold 30px; color: white}
        ''')
        self.label_info_3.setAlignment(Qt.AlignCenter)
        
        self.label_info_4 = QLabel("Es geht los in ")
        self.label_info_4.setStyleSheet('''
        QLabel {font: bold 30px; color: white}
        ''')
        self.label_info_4.setAlignment(Qt.AlignCenter)
        
        self.label_info_5 = QLabel("20")
        self.label_info_5.setStyleSheet('''
        QLabel {font: bold 30px; color: white}
        ''')
        self.label_info_5.setAlignment(Qt.AlignCenter)
        
        self.label_info_6 = QLabel("Los!")
        self.label_info_6.setStyleSheet('''
        QLabel {font: bold 30px; color: white}
        ''')
        self.label_info_6.setAlignment(Qt.AlignCenter)
        
        self.label_info_7 = QLabel("Ergebnis")
        self.label_info_7.setStyleSheet('''
        QLabel {font: bold 30px; color: white}
        ''')
        self.label_info_7.setAlignment(Qt.AlignCenter)        
        
        self.input_answer = QLineEdit()
        self.input_answer.setValidator(QIntValidator())
        self.input_answer.setStyleSheet('''
        QLineEdit {background-color: white; margin: 0 500 0 500}
        ''')
        
        self.count()
        
        # Next button
        self.next_button = QPushButton("Weiter")
        self.next_button.setStyleSheet('''
        QPushButton {margin: 20 200 50 200}
        ''')
        self.next_button.clicked.connect(self.next_page)
        
        
        # Layout
        self.grid = QGridLayout()
        # Left/Right/Bottom layout just used for relative size of central box
        
        # Central box where the content is stored
        self.grid.addWidget(self.label_info_1,0,1,1,3)
        self.grid.addWidget(self.label_info_2,1,1,1,3)
        self.grid.addWidget(self.label_info_3,2,1,1,3)
        self.grid.addWidget(self.label_info_4,3,1,1,3)
        self.grid.addWidget(self.label_info_5,3,1,1,3)
        
        #grid.addWidget(next_button,6,2,5,1)
        
    
        # Central Widget
        widget = QWidget()
        widget.setLayout(self.grid)
        widget.setStyleSheet('''
        QWidget {background-color: #1c1c1c}
        ''')
        self.setCentralWidget(widget)
        self.showMaximized()
    
    def next_page(self):
        self.next_page = ScreenInstructions2(self.name, self.identifier)
        self.close()
    
    def count(self):
        self.gsr_sensor = GroveGSRSensor()
        self.gsr_sensor.startAsyncGSR()
        self.pulse_sensor = Pulsesensor()
        self.pulse_sensor.startAsyncBPM()
        self.qt = QTimer()
        self.qt.timeout.connect(self.timer)
        self.qt.start(1000)
    
    def timer(self):
        '''
        Count up to 20 for preparation time
        count up from 20 to 50 for task preparation
        '''
        # ToDo: implement random next task
        self.i += 1
        if self.i < 20:
            self.label_info_5.setText(str(20 - self.i))
        if self.i == 20:
            self.label_info_1.setParent(None)
            self.label_info_2.setParent(None)
            self.label_info_3.setParent(None)
            self.label_info_4.setParent(None)
            self.label_info_5.setParent(None)
            self.grid.addWidget(self.label_info_6, 4,1,1,3)
        if self.i == 50:
            self.grid.addWidget(self.label_info_7, 0,1,1,3)
            self.grid.addWidget(self.input_answer, 1,1,1,1)
            self.grid.addWidget(QWidget(), 2,1,1,1)
            self.label_info_6.setParent(None)
            print("saving to " + "results/" + self.identifier + self.nr)
            with open("results/" + self.identifier + self.nr + "1", 'w', newline='') as myfile:
                wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
                wr.writerow(self.gsr_sensor.GSR_list)
            with open("results/" + self.identifier + self.nr + "0", 'w', newline='') as myfile:
                wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
                wr.writerow(self.pulse_sensor.BPM_list)
            self.gsr_sensor.stopAsyncGSR()
            self.pulse_sensor.stopAsyncBPM()               
            self.qt.stop()
            #self.next_page()
            return
        
def main():
    app = QApplication(sys.argv)
    info = ScreenTask1Hard("Max Mustermann", "1234")
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()


