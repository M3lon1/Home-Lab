import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from pulse.pulsesensor import Pulsesensor
from grove.grove_gsr_sensor import GroveGSRSensor

class ScreenBaseline(QMainWindow):
    def __init__(self, name, age, sex):
        super().__init__()
        self.name = name
        self.age = age
        self.sex = sex
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle("PsyMex-2 Pilot Studie Baseline")
        
        
        # Labels
        label_info_1 = QLabel("Zur feststellung deiner ruhe Werte führen wir nun eine 30 Sekunden lange Messung durch ")
        label_info_1.setStyleSheet('''
        QLabel {font: bold 30px; color: white}
        ''')
        label_info_1.setAlignment(Qt.AlignCenter)
        
        label_info_2 = QLabel("Schaue hierzu auf das nachfolgende Kreuz")
        label_info_2.setStyleSheet('''
        QLabel {font: bold 30px; color: white}
        ''')
        label_info_2.setAlignment(Qt.AlignCenter)
        
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
        
        grid.addWidget(next_button,3,2,5,1)
        
        # Central Widget
        widget = QWidget()
        widget.setLayout(grid)
        widget.setStyleSheet('''
        QWidget {background-color: #1c1c1c}
        ''')
        self.setCentralWidget(widget)
        self.showMaximized()
    
    def next_page(self):
        pass

def main():
    app = QApplication(sys.argv)
    info = ScreenBaseline("Max Mustermann", 21, "Männlich")
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()