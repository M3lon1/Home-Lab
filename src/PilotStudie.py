import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from pulse.pulsesensor import Pulsesensor
from grove.grove_gsr_sensor import GroveGSRSensor
from ScreenInstructions import *

class PilotStudie(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle("PsyMex-2 Pilot Studie")

        # Labels
        label_welcome = QLabel("Wilkommen zur PsyMex-2 Pilot Studie!")
        label_welcome.setStyleSheet('''
        QLabel {font: bold 30px; color: white}
        ''')
        label_welcome.setAlignment(Qt.AlignCenter)
        
        label_infos = QLabel("Bitte gib uns ein paar Infos zu deiner Person")
        label_infos.setStyleSheet('''
        QLabel {font: 20px; color: white}
        ''')
        label_infos.setAlignment(Qt.AlignCenter)
        
        label_name = QLabel("Name")
        label_name.setStyleSheet('''
        QLabel {color: white}
        ''')
        label_age = QLabel("Alter")
        label_age.setStyleSheet('''
        QLabel {color: white}
        ''')
        label_sex = QLabel("Geschlecht")
        label_sex.setStyleSheet('''
        QLabel {color: white}
        ''')
        # Inputs
        self.input_name = QLineEdit()
        self.input_name.setStyleSheet('''
        QLineEdit {background-color: white}
        ''')
        self.input_age = QLineEdit()
        self.input_age.setValidator(QIntValidator())
        self.input_age.setStyleSheet('''
        QLineEdit {background-color: white}
        ''')
        self.input_sex = QComboBox()
        self.input_sex.addItems(["Weiblich", "Männlich", "Divers"])
        self.input_sex.setStyleSheet('''
        QComboBox {color: #1c1c1c}
        ''')
        # Start button
        start = QPushButton("Weiter")
        start.setStyleSheet('''
        QPushButton {margin: 20 200 50 200}
        ''')
        start.clicked.connect(self.start_studie)
        
        # Layout
        hbox = QHBoxLayout()
        central_box = QVBoxLayout()
        next_box = QVBoxLayout()
        fo = QFormLayout()
        
        central_box.addWidget(label_welcome,1)
        central_box.addWidget(label_infos,1)
        
        fo.addRow(label_name, self.input_name)
        fo.addRow(label_age, self.input_age)
        fo.addRow(label_sex, self.input_sex)
        next_box.addWidget(start)

        central_box.addLayout(fo, 5)
        central_box.addLayout(next_box, 1)
        
        # Layout margins
        central_box.setContentsMargins(50,5,50,5)
        
        # Left/Right layout just used for relative size of central box
        l_layout= QVBoxLayout()
        r_layout = QVBoxLayout()
        hbox.addLayout(l_layout,1)
        hbox.addLayout(central_box,2)
        hbox.addLayout(r_layout,1)
        
        # central widget
        widget = QWidget()
        widget.setLayout(hbox)
        widget.setStyleSheet('''
        QWidget {background-color: #1c1c1c}
        ''')
        
        self.setCentralWidget(widget)
        self.center()
        self.showMaximized()
    
    
    def center(self):
        '''
        move window to screen center
        '''
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
    
    def start_studie(self):
        self.screen_instructions = ScreenInstructions(self.input_name.text(), self.input_age.text(), self.input_sex.currentText())
        self.close()
    
def main():
    app = QApplication(sys.argv)
    pilot = PilotStudie()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()

