import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from pulse.pulsesensor import Pulsesensor
from grove.grove_gsr_sensor import GroveGSRSensor

class PilotStudie(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle("PsyMex-2 Pilot Studie")

        # Labels
        label_welcome = QLabel("Wilkommen zur PsyMex-2 Pilot Studie!")
        label_welcome.setAlignment(Qt.AlignCenter)
        
        # Layout
        vbox = QVBoxLayout()
        vbox.addWidget(label_welcome)
        
        # central widget
        widget = QWidget()
        widget.setLayout(vbox)
        
        self.setCentralWidget(widget)
        self.center()
        self.show()
    
    
    def center(self):
        '''
        move window to screen center
        '''
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

def main():
    app = QApplication(sys.argv)
    pilot = PilotStudie()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()