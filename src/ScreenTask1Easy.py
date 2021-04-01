import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from pulse.pulsesensor import Pulsesensor
from grove.grove_gsr_sensor import GroveGSRSensor
from ScreenInstructions2 import *

class ScreenTask1Easy(QMainWindow):
    def __init__(self, name, identifier):
        super().__init__()
        self.name = name
        self.identifier = identifier
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle("PsyMex-2 Pilot Aufgabe 1 leicht")
        self.i = 20
        
        # Labels
        label_info_1 = QLabel("Aufgabe 1 leicht")
        label_info_1.setStyleSheet('''
        QLabel {font: bold 30px; color: white}
        ''')
        label_info_1.setAlignment(Qt.AlignCenter)
        
        label_info_2 = QLabel("Summiere die Zahl 3 im Kopf auf bis die Zeit vorbei ist")
        label_info_2.setStyleSheet('''
        QLabel {font: bold 30px; color: white}
        ''')
        label_info_2.setAlignment(Qt.AlignCenter)        
        
        label_info_3 = QLabel("Es geht los in ")
        label_info_3.setStyleSheet('''
        QLabel {font: bold 30px; color: white}
        ''')
        label_info_3.setAlignment(Qt.AlignCenter)
        
        self.label_info_4 = QLabel("20")
        self.label_info_4.setStyleSheet('''
        QLabel {font: bold 30px; color: white}
        ''')
        self.label_info_4.setAlignment(Qt.AlignCenter)
        
        self.count()
        
        # Next button
        next_button = QPushButton("Weiter")
        next_button.setStyleSheet('''
        QPushButton {margin: 20 200 50 200}
        ''')
        next_button.clicked.connect(self.next_page)
        
        
        # Layout
        self.grid = QGridLayout()
        # Left/Right/Bottom layout just used for relative size of central box
        
        # Central box where the content is stored
        self.grid.addWidget(label_info_1,0,1,1,3)
        self.grid.addWidget(label_info_2,1,1,1,3)
        self.grid.addWidget(label_info_3,2,1,1,3)
        self.grid.addWidget(self.label_info_4,3,1,1,3)
        
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
        self.qt = QTimer()
        self.qt.timeout.connect(self.timer)
        self.qt.start(1000)
    
    def timer(self):
        self.i -= 1
        self.label_info_4.setText(str(self.i))
        if self.i == 0:
            self.qt.stop()
            return
        
def main():
    app = QApplication(sys.argv)
    info = ScreenTask1Easy("Max Mustermann", "1234")
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()

