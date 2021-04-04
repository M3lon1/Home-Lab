import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from pulse.pulsesensor import Pulsesensor
from grove.grove_gsr_sensor import GroveGSRSensor
from PyQt5.QtGui import *
import csv
from ScreenInstructions2 import *

class ScreenEnd(QMainWindow):
    def __init__(self, name):
        super().__init__()
        self.name = name
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle("PsyMex-2 Pilot Aufgabe 1 leicht")
        self.i = 0
        
        # Labels
        self.label_info_1 = QLabel("Vielen Dank für deine Teilnahme " + self.name)
        self.label_info_1.setStyleSheet('''
        QLabel {font: bold 30px; color: white}
        ''')
        self.label_info_1.setAlignment(Qt.AlignCenter)
    
        
        
        # Layout
        self.grid = QGridLayout()
        # Left/Right/Bottom layout just used for relative size of central box
        
        # Central box where the content is stored
        self.grid.addWidget(self.label_info_1,0,1,1,3)
    
        # Central Widget
        widget = QWidget()
        widget.setLayout(self.grid)
        widget.setStyleSheet('''
        QWidget {background-color: #1c1c1c}
        ''')
        self.setCentralWidget(widget)
        self.showMaximized()

        
def main():
    app = QApplication(sys.argv)
    info = ScreenEnd("Max Mustermann", "1234", [])
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()


