import sys
from PyQt5.QtWidgets import *
#from PyQt5.QtGui import *
from PyQt5.QtCore import *
from matplotlib.backends.backend_qt5agg import FigureCanvas
import matplotlib as mpl
import matplotlib.figure as mpl_fig
import matplotlib.animation as anim
import numpy as np

class Window(QWidget):
    '''
    This is the main Window Class
    '''
    def __init__(self):
        super().__init__()
        self.setWindowTitle('PsyMex-2')
        self.setStyleSheet('QWidget { background-color: #212121; }')
        self.width = self.frameGeometry().width()
        self.height = self.frameGeometry().height()
        
        # Dashboard button
        button_home = QPushButton('Dashboard')
        button_home.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        button_home.setStyleSheet('''
        QPushButton {color: #82ECF0; border: none; font: 20px}
        QPushButton:pressed {color: #82ECFF; font: bold 20px;}
        ''') # Border needs to be set to none to change background
        #button_home.setStyleSheet('QPushButton:pressed {border-style: outset; border-width: 2px; border-radius: 10px; border-color: #424242; font: bold 20px }')
        # Heart Rate button
        button_hr = QPushButton('Heart Rate')
        button_hr.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        button_hr.setStyleSheet('''
        QPushButton {color: #82ECF0; border: none; font: 20px}
        QPushButton:pressed {color: #82ECFF; font: bold 20px;}
        ''')
        # Heart Rate button
        button_gsr = QPushButton('Skin Conductance')
        button_gsr.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        button_gsr.setStyleSheet('''
        QPushButton {color: #82ECF0; border: none; font: 20px}
        QPushButton:pressed {color: #82ECFF; font: bold 20px;}
        ''')
        
        # PsyMex-2 icon
        psymex_label = QLabel('<h1>PsyMex-2</h1>')
        psymex_label.setStyleSheet('color: #00D4DB; font: bold 20px')
        
        # Layouts
        outer_layout = QHBoxLayout()
        left_bar = QVBoxLayout()
        
        # Psymex icon layout
        psymex_layout = QVBoxLayout()
        psymex_layout.setAlignment(Qt.AlignCenter)
        psymex_layout.setContentsMargins(5,5,5,5)
        psymex_layout.addWidget(psymex_label)
        
        # Menu Layout Vertical Box
        menu_layout = QVBoxLayout()
        menu_layout.setSpacing(5)
        menu_layout.setContentsMargins(5,5,5,5) # left top right bottom
        menu_layout.addWidget(button_home, 1)
        menu_layout.addWidget(button_hr, 1)
        menu_layout.addWidget(button_gsr, 1)
        
        # Plot Layout Horizontal Box
        view = QVBoxLayout()
        plot_hr = MyFigureCanvas(10,10)
        view.addWidget(plot_hr)
        
        plot_gsr = MyFigureCanvas(2,2)
        view.addWidget(plot_gsr)
        
        # Building overal Layout
        left_bar.addLayout(psymex_layout, 1)
        left_bar.addLayout(menu_layout, 2)
        outer_layout.addLayout(left_bar,1)
        outer_layout.addLayout(view, 4)
        
        self.setLayout(outer_layout)
        

class MyFigureCanvas(FigureCanvas, anim.FuncAnimation):
    '''
    This is the FigureCanvas in which the live plot is drawn
    '''
    def __init__(self, x_dim, y_dim):
        
        FigureCanvas.__init__(self, mpl_fig.Figure())
        self.ax = self.figure.subplots()
        self.ax.set_ylim(ymin=0, ymax=y_dim)
        self.ax.set_xlim(xmin=0, xmax=x_dim)
        self.line,  = self.ax.plot([], [], lw=2)
        
        anim.FuncAnimation.__init__(self, self.figure, self.update_canvas,frames=200, interval=20, blit=True)
    
    def update_canvas(self, i):
        # Get data values from 
        x = 0
        y = 0
        self.line.set_data(x,y)
        return self.line
        
def main():
    app = QApplication(sys.argv)
    GUI = Window()
    GUI.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()