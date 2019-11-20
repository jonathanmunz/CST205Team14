#CALCULATOR
import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QVBoxLayout,
                            QHBoxLayout, QPushButton, QComboBox, QLineEdit, QSlider,QGridLayout)
from PyQt5.QtCore import pyqtSlot, Qt
import numpy as np
import cv2
import threading
from collections import deque
from pygame import mixer

class Window(QWidget):
    def __init__(self):
        super().__init__()
        mixer.init()
        self.setStyleSheet(open('css/style.css').read())

        # Window Title
        self.setWindowTitle("Calculator")
        # self.drawing_message = QLabel("These are the coloring options:")
        # self.other_message = QLabel("These are all the other options:")

        self.color_message = QLabel("Welcome to Calculator.")

        # Colors Combobox
        options = ["Basic", "Scientific", "Graphing"]
        self.choose_calc = QComboBox()
        self.choose_calc.addItems(options)
        self.choose_calc.currentIndexChanged.connect(self.calc_chosen)

        #Create the coloring options section
        self.coloring_options = QVBoxLayout()
        self.coloring_options.addWidget(self.color_message)
        self.coloring_options.addWidget(self.choose_calc)

        #Put the two option squares side by side
        self.hbox = QHBoxLayout()
        self.hbox.addLayout(self.coloring_options)

        # Window Setup
        self.vbox = QVBoxLayout()
        self.vbox.addLayout(self.hbox)
        self.setLayout(self.vbox)


    @pyqtSlot()
    def calc_chosen(self):
        calcChosen = self.choose_calc.currentText()
        self.titleMessage = QLabel('')
        if(calcChosen == 'Basic'):
        	self.titleMessage.setText('Basic Calculator')
        	self.basic_calc()
        elif calcChosen == 'Scientific':
            self.titleMessage.setText('Scientific Calculator')
        elif calcChosen == 'Graphing':
            self.titleMessage.setText('Graphing Calculator')


    @pyqtSlot()
    def basic_calc(self):
    	textBox = QLineEdit()

    	#numbers
    	self.one = QPushButton('1')
    	self.two = QPushButton('2')
    	self.three = QPushButton('3')
    	self.four = QPushButton('4')
    	self.five = QPushButton('5')
    	self.six = QPushButton('6')
    	self.seven = QPushButton('7')
    	self.eight = QPushButton('8')
    	self.nine = QPushButton('9')
    	self.zero = QPushButton('0')

    	#Symbols
    	self.clear = QPushButton('C')
    	self.add = QPushButton('+')
    	self.subtract = QPushButton('-')
    	self.divide = QPushButton('/')
    	self.equals = QPushButton('=')
    	self.period = QPushButton('.')
    	self.negative = QPushButton('+/-')


    	self.numLayout = QGridLayout()
    	self.numLayout.setColumnStretch(1, 4)
    	self.numLayout.setColumnStretch(2,4)
    	self.numLayout.addWidget(self.clear)
    	self.numLayout.addWidget(self.seven)
    	self.numLayout.addWidget(self.eight)
    	self.numLayout.addWidget(self.nine)
    	self.numLayout.addWidget(self.four)
    	self.numLayout.addWidget(self.five)
    	self.numLayout.addWidget(self.six)
    	self.numLayout.addWidget(self.one)
    	self.numLayout.addWidget(self.two)
    	self.numLayout.addWidget(self.three)
    	self.numLayout.addWidget(self.zero)
    	self.numLayout.addWidget(self.period)
    	self.numLayout.addWidget(self.negative)

    	self.vbox.addLayout(self.numLayout)


app = QApplication(sys.argv)
main = Window()
p =  main.palette()
p.setColor(main.backgroundRole(), Qt.black)
main.setPalette(p)
main.show()
sys.exit(app.exec_())