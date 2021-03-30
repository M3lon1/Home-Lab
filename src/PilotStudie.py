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
        input_name = QLineEdit()
        input_name.setStyleSheet('''
        QLineEdit {background-color: white}
        ''')
        input_age = QLineEdit()
        input_age.setStyleSheet('''
        QLineEdit {background-color: white}
        ''')
        input_gender = QComboBox()
        input_gender.addItems(["Weiblich", "Männlich", "Divers"])
        input_gender.setStyleSheet('''
        QComboBox {color: #1c1c1c}
        ''')
        # Start button
        start = QPushButton("Start")
        start.setStyleSheet('''
        QPushButton {margin: 20 200 50 200}
        ''')
        start.clicked.connect(self.start_studie)
        
        # Layout
        hbox = QHBoxLayout()
        central_box = QVBoxLayout()
        fo = QFormLayout()
        
        central_box.addWidget(label_welcome,1)
        central_box.addWidget(label_infos,1)
        
        fo.addRow(label_name, input_name)
        fo.addRow(label_age, input_age)
        fo.addRow(label_sex, input_gender)
        fo.addRow(start)

        central_box.addLayout(fo, 5)
        
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
        self.show()
    
    
    def center(self):
        '''
        move window to screen center
        '''
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
    
    def start_studie(self):
        pass
    
def main():
    app = QApplication(sys.argv)
    pilot = PilotStudie()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()