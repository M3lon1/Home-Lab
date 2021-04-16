import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from pulse.pulsesensor import Pulsesensor
from grove.grove_gsr_sensor import GroveGSRSensor
from ScreenInstructions2 import *

class ScreenInstructions(QMainWindow):
    def __init__(self, name, identifier):
        super().__init__()
        self.name = name
        self.identifier = identifier
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle("PsyMex-2 Pilot Studie Instructuions")
        
        
        # Labels
        label_info_1 = QLabel("Ablauf der Studie")
        label_info_1.setStyleSheet('''
        QLabel {font: bold 30px; color: white}
        ''')
        label_info_1.setAlignment(Qt.AlignCenter)
        
        label_info_2 = QLabel("Es gibt insgesamt 3 Aufgaben in 2 Schwierigkeitsstufen")
        label_info_2.setStyleSheet('''
        QLabel {font: bold 30px; color: white}
        ''')
        label_info_2.setAlignment(Qt.AlignCenter)
        
        label_info_3 = QLabel("Die Aufgaben stammen jeweils aus einer Kategorie (Motorisch, Affektiv, Kognitiv)")
        label_info_3.setStyleSheet('''
        QLabel {font: bold 30px; color: white}
        ''')
        label_info_3.setAlignment(Qt.AlignCenter)
        
        label_info_4 = QLabel("Vor jeder Aufgabe gibt es Zeit zum Einlesen")
        label_info_4.setStyleSheet('''
        QLabel {font: bold 30px; color: white}
        ''')
        label_info_4.setAlignment(Qt.AlignCenter)
        
        label_info_5 = QLabel("Danach wird die Aufgabe für 30 Sekunden ausgeführt, gefolgt von einer 30 Sekunden Ruhephase")
        label_info_5.setStyleSheet('''
        QLabel {font: bold 30px; color: white}
        ''')
        label_info_5.setAlignment(Qt.AlignCenter)
        
        label_info_6 = QLabel("Der genaue Ablauf sieht wie folgt aus")
        label_info_6.setStyleSheet('''
        QLabel {font: bold 30px; color: white}
        ''')
        label_info_6.setAlignment(Qt.AlignCenter)
        
        # Next button
        next_button = QPushButton("Weiter")
        next_button.setStyleSheet('''
        QPushButton {margin: 20 200 50 200}
        ''')
        next_button.clicked.connect(self.next_page)
        
        
        # Layout
        grid = QGridLayout()
        # Left/Right/Bottom layout just used for relative size of central box
        
        # Central box where the content is stored
        grid.addWidget(label_info_1,0,1,1,3)
        grid.addWidget(label_info_2,1,1,1,3)
        grid.addWidget(label_info_3,2,1,1,3)
        grid.addWidget(label_info_4,3,1,1,3)
        grid.addWidget(label_info_5,4,1,1,3)
        grid.addWidget(label_info_6,5,1,1,3)
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
        self.next_page = ScreenInstructions2(self.name, self.identifier)
        self.close()
        

def main():
    app = QApplication(sys.argv)
    info = ScreenInstructions("Max Mustermann", "1234")
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
