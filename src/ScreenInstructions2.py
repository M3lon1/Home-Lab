import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from pulse.pulsesensor import Pulsesensor
from grove.grove_gsr_sensor import GroveGSRSensor
from ScreenBaseline import *

class ScreenInstructions2(QMainWindow):
    def __init__(self, name, identifier):
        super().__init__()
        self.name = name
        self.identifier = identifier
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle("PsyMex-2 Pilot Studie Instructions")
        
        
        # Labels
        label_info_1 = QLabel("1. Baseline messung, 30 Sek")
        label_info_1.setStyleSheet('''
        QLabel {font: bold 30px; color: white}
        ''')
        label_info_1.setAlignment(Qt.AlignCenter)
        
        label_info_2 = QLabel("2. Aufgabe 1, 30 Sek")
        label_info_2.setStyleSheet('''
        QLabel {font: bold 30px; color: white}
        ''')
        label_info_2.setAlignment(Qt.AlignCenter)
        
        label_info_3 = QLabel("3. Pause, 30 Sek")
        label_info_3.setStyleSheet('''
        QLabel {font: bold 30px; color: white}
        ''')
        label_info_3.setAlignment(Qt.AlignCenter)
        
        label_info_4 = QLabel("Schritt 2 und 3 werden werden wiederholt bis alle 6 Aufgaben durlaufen sind")
        label_info_4.setStyleSheet('''
        QLabel {font: bold 30px; color: white}
        ''')
        label_info_4.setAlignment(Qt.AlignCenter)
        
        # Next button
        next_button = QPushButton("Weiter")
        next_button.setStyleSheet('''
        QPushButton {margin: 20 200 50 200}
        ''')
        next_button.clicked.connect(self.next_page)
        
        # Layout
        
        # Layout
        grid = QGridLayout()
        # Left/Right/Bottom layout just used for relative size of central box
        
        # Central box where the content is stored
        grid.addWidget(label_info_1,0,1,1,3)
        grid.addWidget(label_info_2,1,1,1,3)
        grid.addWidget(label_info_3,2,1,1,3)
        grid.addWidget(label_info_4,3,1,1,3)
        grid.addWidget(next_button,6,2,5,1)
        
        # Bottom widget just for relative size
        bottom_widget = QWidget()
        
        # Central Widget
        widget = QWidget()
        widget.setLayout(grid)
        widget.setStyleSheet('''
        QWidget {background-color: #1c1c1c}
        ''')
        self.setCentralWidget(widget)
        self.showMaximized()
    
    def next_page(self):
        self.next_screen = ScreenBaseline(self.name, self.identifier)
        self.close()
        
        

def main():
    app = QApplication(sys.argv)
    info = ScreenInstructions2("Max Mustermann","123455")
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()

