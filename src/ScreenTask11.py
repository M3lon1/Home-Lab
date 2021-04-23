import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from pulse.pulsesensor import Pulsesensor
from grove.grove_gsr_sensor import GroveGSRSensor
from PyQt5.QtGui import *
import csv
import random
from ScreenEnd import *


class ScreenTask11(QMainWindow):
    def __init__(self, name, identifier, tasks):
        super().__init__()
        self.name = name # name of participant
        self.identifier = identifier # string for saving the files
        self.nr = "11" # task number, first digit = task second digit = hard/easy 1 = easy 2 = hard
        self.tasks = tasks # list of tasks to still perform
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle("PsyMex-2 Pilot Aufgabe 1 leicht")
        self.i = 0 # counter for preparation time & execution time
        
        # Labels
        self.label_info_1 = QLabel("Aufgabe 1 Leicht")
        self.label_info_1.setStyleSheet('''
        QLabel {font: bold 30px; color: white}
        ''')
        self.label_info_1.setAlignment(Qt.AlignCenter)
        
        self.label_info_2 = QLabel("Summiere die Zahl 3 im Kopf auf bis die Zeit vorbei ist")
        self.label_info_2.setStyleSheet('''
        QLabel {font: bold 30px; color: white}
        ''')
        self.label_info_2.setAlignment(Qt.AlignCenter)        
        
        self.label_info_3 = QLabel("Es geht los in ")
        self.label_info_3.setStyleSheet('''
        QLabel {font: bold 30px; color: white}
        ''')
        self.label_info_3.setAlignment(Qt.AlignCenter)
        
        self.label_info_4 = QLabel("20")
        self.label_info_4.setStyleSheet('''
        QLabel {font: bold 30px; color: white}
        ''')
        self.label_info_4.setAlignment(Qt.AlignCenter)##
        
        self.label_info_5 = QLabel("Los!")
        self.label_info_5.setStyleSheet('''
        QLabel {font: bold 30px; color: white}
        ''')
        self.label_info_5.setAlignment(Qt.AlignCenter)
        
        self.label_info_6 = QLabel("Ergebnis")
        self.label_info_6.setStyleSheet('''
        QLabel {font: bold 30px; color: white}
        ''')
        self.label_info_6.setAlignment(Qt.AlignCenter)
        
        self.input_answer = QLineEdit()
        self.input_answer.setValidator(QIntValidator())
        self.input_answer.setStyleSheet('''
        QLineEdit {background-color: white; margin: 0 500 0 500}
        ''')
        
        self.label_info_7 = QLabel("+")
        self.label_info_7.setStyleSheet('''
        QLabel {font: bold 50px; color: white}
        ''')
        self.label_info_7.setAlignment(Qt.AlignCenter)
        
        self.count()
        
        # Next button
        self.next_button = QPushButton("Weiter")
        self.next_button.setStyleSheet('''
        QPushButton {margin: 20 200 50 200}
        ''')
        self.next_button.clicked.connect(self.next_page)
        
        
        # Layout
        self.grid = QGridLayout()
        
        # Central box where the content is stored
        self.grid.addWidget(self.label_info_1,0,1,1,3)
        self.grid.addWidget(self.label_info_2,1,1,1,3)
        self.grid.addWidget(self.label_info_3,2,1,1,3)
        self.grid.addWidget(self.label_info_4,3,1,1,3)
    
        # Central Widget
        widget = QWidget()
        widget.setLayout(self.grid)
        widget.setStyleSheet('''
        QWidget {background-color: #1c1c1c}
        ''')
        self.setCentralWidget(widget)
        self.showMaximized()
    
    def next_page(self):
        '''
        Function to chose what page is going to be next.
        Picks from self.tasks
        '''
        # Before continue get the answer for the current task and save it 
        if self.input_answer.text() != '':
            with open("results/" + self.identifier + self.nr + "2", 'w', newline='') as myfile:
                wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
                wr.writerows(self.input_answer.text())
            # Check if there are tasks left
            if len(self.tasks) != 0: 
                for item in self.tasks:
                    # Check if the corresponding hard/easy task is still available
                    if "ScreenTask" + self.nr[0] == item[0:-1]:
                        class_name = item
                        module = __import__(item)
                        class_ = getattr(module, class_name)
                        self.instance = class_(self.name, self.identifier, self.tasks)
                        self.tasks.remove(item)
                        self.close()
                        return
                # If task is not found, pick a random next task    
                i = random.randint(0, len(self.tasks) - 1)
                class_name = self.tasks[i]
                module = __import__(self.tasks[i])
                class_ = getattr(module, class_name)
                self.instance = class_(self.name, self.identifier, self.tasks)
                del self.tasks[i]
                self.close()
                return
            else:
                # If there are no tasks left, show end screen
                module = __import__("ScreenEnd")
                class_ = getattr(module, "ScreenEnd")
                self.instance = class_(self.name)
                self.close()
        else:
            # if there is no input from the user just wait for it
            pass
        
    def count(self):
        '''
        Function to start the sensors and QTimer for measuring
        '''
        self.gsr_sensor = GroveGSRSensor()
        self.gsr_sensor.startAsyncGSR()
        self.pulse_sensor = Pulsesensor()
        self.pulse_sensor.startAsyncBPM()
        self.qt = QTimer()
        # Timer calls self.timer() every second
        self.qt.timeout.connect(self.timer)
        self.qt.start(1000)
    
    def timer(self):
        '''
        Count up to 20 for preparation time
        count up from 20 to 50 for task preparation
        '''
        # ToDo: implement random next task
        self.i += 1
        if self.i < 20:
            # count down for preparation time
            self.label_info_4.setText(str(20 - self.i))
        if self.i == 20:
            # Remove all Widgets currently displayed. Task starts
            self.label_info_1.setParent(None)
            self.label_info_2.setParent(None)
            self.label_info_3.setParent(None)
            self.label_info_4.setParent(None)
            self.grid.addWidget(self.label_info_5, 4,1,1,3)
            print(self.i)
        if self.i == 50:
            self.label_info_5.setParent(None)
            self.label_info_7.setText('Pause')
            self.grid.addWidget(self.label_info_7)
        if self.i == 80:
            self.label_info_7.setParent(None)
            self.grid.addWidget(self.label_info_6, 0,1,1,1, Qt.AlignCenter)
            self.grid.addWidget(self.input_answer, 1,1,1,1, Qt.AlignCenter)
            self.grid.addWidget(QWidget(), 2,1,1,1, Qt.AlignCenter)
            self.grid.addWidget(self.next_button, 3,1,1,1, Qt.AlignCenter)
            self.label_info_5.setParent(None)
            print("saving to " + "results/" + self.identifier + str(self.nr))
            # saving files to results folder.
            #last digit specify which sensor type it is 1 = GSR 0 = HR or Answer
            with open("results/" + self.identifier + self.nr + "1", 'w', newline='') as myfile:
                wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
                wr.writerows(self.gsr_sensor.GSR_list)
            with open("results/" + self.identifier + self.nr + "0", 'w', newline='') as myfile:
                wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
                wr.writerows(self.pulse_sensor.BPM_list)
            # Stop the sensors
            self.gsr_sensor.stopAsyncGSR()
            self.pulse_sensor.stopAsyncBPM()               
            self.qt.stop()
            return
        
def main():
    app = QApplication(sys.argv)
    info = ScreenTask11("Max Mustermann", "22.04.to.", [])
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()

