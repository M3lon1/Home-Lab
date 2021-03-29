import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from pulse.pulsesensor import Pulsesensor
from grove.grove_gsr_sensor import GroveGSRSensor

class PilotStudie(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("PsyMex-2 Pilot Studie")
        
        # move to center of screen
        qtRectangle = self.frameGeometry()
        centerPoint = QDesktopWidget().availableGeometry().center()
        qtRectangle.moveCenter(centerPoint)
        self.move(qtRectangle.center)
        
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
        self.show()



def main():
    app = QApplication(sys.argv)
    pilot = PilotStudie()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()