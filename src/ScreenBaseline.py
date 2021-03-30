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
        
        # Layout
        hbox = QHBoxLayout()
        central_box = QVBoxLayout()
        
        # Central box where the content is stored
        central_box.addWidget(label_info_1,1)
        central_box.addWidget(label_info_2)
        
        # Bottom widget just for relative size
        bottom_widget = QWidget()
        central_box.addWidget(bottom_widget, 3)
        
        # Layout margins
        central_box.setContentsMargins(50,5,50,5)
        
        # Left/Right/Bottom layout just used for relative size of central box
        l_layout= QVBoxLayout()
        r_layout = QVBoxLayout()
        hbox.addLayout(l_layout,1)
        hbox.addLayout(central_box,2)
        hbox.addLayout(r_layout,1)
        
        # Central Widget
        widget = QWidget()
        widget.setLayout(hbox)
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