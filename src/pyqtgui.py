import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class Window(QtGui.QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.setGeometry(100, 100, 280, 80)
        self.setWindowTitle('PsyMex-2')
        self.home()
        
    def home():
        # Dashboard button
        button_Home = QPushButton('Dashboard', window)
        button_Home.resize(window_width/10, window_height/10)
        # Heart Rate button
        button_Hr = QPushButton('Heart Rate', window)
        button_Hr.resize(window_width/10, window_height/10)

def run():
    app = QApplication(sys.argv)
    GUI = Window()
    sys.exit(app.exec_())

if __name__ == "__main__":
    run()