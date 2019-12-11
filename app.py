#! /usr/bin/env python


#CALCULATOR
import sys
import math
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QVBoxLayout,
                            QHBoxLayout, QPushButton, QComboBox, QTextEdit, QSlider,QGridLayout,QMainWindow)
from PyQt5.QtCore import pyqtSlot, Qt
import numpy as np
import threading
from collections import deque
from functools import partial



ERROR_MSG = "ERROR"

class calcGui(QMainWindow): # QMainWindow Class for the calculator GUI

    def __init__(self):
        super().__init__()
        #self.setStyleSheet(open('css/style.css').read())
        self.model = evaluateProblem
        self.cc = CalcController(self.model, self)

        # Set Main Window Title
        self.setWindowTitle("Calculator")
        #Setting the main widget and the layout that will be used for the calculator
        self.mainWidget = QWidget(self)
        self.setCentralWidget(self.mainWidget)
        #Main layout for the window
        self.mainLayout = QVBoxLayout()
        #Put the two dropdowns side by side in horizontal layout
        self.selectionLayout = QHBoxLayout()
        #Grid layout for the buttons
        self.buttonsGrid = QGridLayout()
        #set layout for the widget
        self.mainWidget.setLayout(self.mainLayout)
    
        #create the buttons, dropdown, screen, etc.
        self.createDisplay()
        self.createDropDowns()
        self.createInitialButtons()
        
        #self.color_message = QLabel("Welcome to Calculator.")

        #Create the coloring options section
        #self.coloring_options.addWidget(self.color_message)

        
    def createDropDowns(self):
        
        #dropdown for calculator mode
        self.modeDropDown = QVBoxLayout()
        self.selectModeLabel = QLabel("Select Mode")
        calcType = ["Basic", "Scientific", "Subnet"]
        self.choose_calc = QComboBox()
        self.choose_calc.setFixedHeight(40)
        self.choose_calc.addItems(calcType)
        self.choose_calc.currentIndexChanged.connect(self.calc_chosen)
        self.modeDropDown.addWidget(self.selectModeLabel)
        self.modeDropDown.addWidget(self.choose_calc)
        self.selectionLayout.addLayout(self.modeDropDown)
        
        #dropdown for color theme
        self.colorDropDown = QVBoxLayout()
        self.selectColorLabel = QLabel("Select Color")
        calcTheme = ["1", "2", "3", "4"]
        self.choose_theme = QComboBox()
        self.choose_theme.setFixedHeight(40)
        self.choose_theme.addItems(calcTheme)
        self.choose_theme.currentIndexChanged.connect(self.theme_chosen)
        self.colorDropDown.addWidget(self.selectColorLabel)
        self.colorDropDown.addWidget(self.choose_theme)
        self.selectionLayout.addLayout(self.colorDropDown)
        
        #add the dropdowns horizontal layout to the main layout
        self.mainLayout.addLayout(self.selectionLayout)

        
    def createDisplay(self):
        # Create the display widget
        self.display = QTextEdit()
        # Set some display's properties
        self.display.setFixedHeight(60)
        self.display.setAlignment(Qt.AlignRight)
        # Add the display to the main layout
        self.mainLayout.addWidget(self.display)

    @pyqtSlot()
    def theme_chosen(self):
        themeChosen = self.choose_theme.currentText()
        
        if(themeChosen == '1'):
            self.setStyleSheet(open('css/style.css').read())
            
        elif themeChosen == '2':
            self.setStyleSheet(open('css/style2.css').read())



    @pyqtSlot()
    def calc_chosen(self):
        calcChosen = self.choose_calc.currentText()
        
        if(calcChosen == 'Basic'):
        
            self.setWindowTitle('Basic Calculator')
            self.display.setFixedHeight(60)
            self.destroyButtons()
            self.createBasicButtons()
        elif calcChosen == 'Scientific':
            self.setWindowTitle('Scientific Calculator')
            self.destroyButtons()
            self.createScientificButtons()
        elif calcChosen == 'Subnet':
            self.setWindowTitle('Subnet Calculator')
            self.display.setFixedHeight(180)
            self.destroyButtons()
            self.createSubnetButtons()
            
            
            
    def setDisplayText(self, text):
        self.display.setText(text)
        self.display.repaint()
        
    def getDisplayText(self):
        """Get display's text."""
        return self.display.toPlainText()

    def clearDisplay(self):
        """Clear the display."""
        self.setDisplayText("")
        
    @pyqtSlot()
    def destroyButtons(self):
        for i in reversed(range(self.buttonsGrid.count())):
            widgetToRemove = self.buttonsGrid.itemAt(i).widget()
            # remove it from the layout list
            self.buttonsGrid.removeWidget(widgetToRemove)
            # remove it from the gui
            widgetToRemove.setParent(None)
    
    def createInitialButtons(self):
        """Create the buttons."""
        self.buttons = {}
        # Button text | position on the QGridLayout
        buttons = {
            "7": (0, 0),
            "8": (0, 1),
            "9": (0, 2),
            "/": (0, 3),
            "C": (0, 4),
            "4": (1, 0),
            "5": (1, 1),
            "6": (1, 2),
            "*": (1, 3),
            "(": (1, 4),
            "1": (2, 0),
            "2": (2, 1),
            "3": (2, 2),
            "-": (2, 3),
            ")": (2, 4),
            "0": (3, 0),
            "00": (3, 1),
            ".": (3, 2),
            "+": (3, 3),
            "=": (3, 4),
        }
        # Create the buttons and add them to the button grid layout
        for btnText, pos in buttons.items():
            self.buttons[btnText] = QPushButton(btnText)
            self.buttons[btnText].setFixedSize(80, 80)
            self.buttonsGrid.addWidget(self.buttons[btnText], pos[0], pos[1])
            

        # Add buttonsGrid to the Main layout
        self.mainLayout.addLayout(self.buttonsGrid)
        self.cc.connectButtons()
        self.buttons["="].clicked.connect(self.cc._calculateResult)

    
    @pyqtSlot()
    def createBasicButtons(self):
        """Create the buttons."""
        self.buttons = {}
        #buttonsGrid = QGridLayout()
        # Button text | position on the QGridLayout
        buttons = {
            "7": (0, 0),
            "8": (0, 1),
            "9": (0, 2),
            "/": (0, 3),
            "C": (0, 4),
            "4": (1, 0),
            "5": (1, 1),
            "6": (1, 2),
            "*": (1, 3),
            "(": (1, 4),
            "1": (2, 0),
            "2": (2, 1),
            "3": (2, 2),
            "-": (2, 3),
            ")": (2, 4),
            "0": (3, 0),
            "00": (3, 1),
            ".": (3, 2),
            "+": (3, 3),
            "=": (3, 4),
        }
        # Create the buttons and add them to the button grid layout
        for btnText, pos in buttons.items():
            self.buttons[btnText] = QPushButton(btnText)
            self.buttons[btnText].setFixedSize(80, 80)
            self.buttonsGrid.addWidget(self.buttons[btnText], pos[0], pos[1])
            
        self.cc.connectButtons()
        self.buttons["="].clicked.connect(self.cc._calculateResult)

    @pyqtSlot()
    def createScientificButtons(self):
        """Create the buttons."""
        self.buttons = {}
        #buttonsGrid = QGridLayout()
        # Button text | position on the QGridLayout
        buttons = {
            "7": (0, 0),
            "8": (0, 1),
            "9": (0, 2),
            "sin": (0,3),
            "/": (0, 4),
            "C": (0, 5),
            "4": (1, 0),
            "5": (1, 1),
            "6": (1, 2),
            "cos": (1,3),
            "*": (1, 4),
            "(": (1, 5),
            "1": (2, 0),
            "2": (2, 1),
            "3": (2, 2),
            "tan": (2,3),
            "-": (2, 4),
            ")": (2, 5),
            "0": (3, 0),
            "00": (3, 1),
            ".": (3, 2),
            "^": (3,3),
            "+": (3, 4),
            "=": (3, 5),
        }
        # Create the buttons and add them to the button grid layout
        for btnText, pos in buttons.items():
            self.buttons[btnText] = QPushButton(btnText)
            self.buttons[btnText].setFixedSize(80, 80)
            self.buttonsGrid.addWidget(self.buttons[btnText], pos[0], pos[1])
            
        self.cc.connectButtons()
        self.buttons["="].clicked.connect(self.cc._calculateResult)
        
    @pyqtSlot()
    def createSubnetButtons(self):
        """Create the buttons."""
        self.buttons = {}
        # Button text | position on the QGridLayout
        buttons = {
            "7": (0, 0),
            "8": (0, 1),
            "9": (0, 2),
            "/": (0, 3),
            "C": (0, 4),
            "4": (1, 0),
            "5": (1, 1),
            "6": (1, 2),
            "0": (1, 3),
            "00": (1, 4),
            "1": (2, 0),
            "2": (2, 1),
            "3": (2, 2),
            ".": (2, 3),
            "SUBNET": (2, 4),
        }
        # Create the buttons and add them to the button grid layout
        for btnText, pos in buttons.items():
            self.buttons[btnText] = QPushButton(btnText)
            self.buttons[btnText].setFixedSize(80, 80)
            self.buttonsGrid.addWidget(self.buttons[btnText], pos[0], pos[1])
            
        self.cc.connectButtons()
        self.buttons["SUBNET"].clicked.connect(self.cc._subnetResult)




# Controller Class for the Calculator
class CalcController:

    def __init__(self, model, view):
    
        #model instance
        self.evaluateProblem = model
        
        self.mainView = view
        # connect the buttons to functions
        #self.connectButtons()
        
        
    def connectButtons(self):
        for btnText, btn in self.mainView.buttons.items():
            if btnText not in {"=", "C", "SUBNET"}:
                btn.clicked.connect(partial(self._buildExpression, btnText))
                
        #self.mainView.display.returnPressed.connect(self._calculateResult)
        self.mainView.buttons["C"].clicked.connect(self.mainView.clearDisplay)
        
    def _subnetResult(self):
        #Data Structures
        subnetAddress = []
        screenText = ""
        userInput = self.mainView.getDisplayText()
        inputList = userInput.split('/')
        ip, sNet = inputList[0], inputList[1]
        ip = ip.split('.')
        ip.append(sNet)
        ipAddress = [int(convert) for convert in ip]

        #Store the ip address and mask into subnetAddress
        for item in ipAddress:
            subnetAddress.append(item)

        #Calculate the classful subnet mask
        subnetMask = ipAddress[-1]

        if(subnetMask >= 24):
            classfulSubnetMask = 24
            nClass = 'C'

        elif(subnetMask >= 16):
            classfulSubnetMask = 16
            nClass = 'B'

        elif(subnetMask >= 8):
            classfulSubnetMask = 8
            nClass = 'A'

        #Create lists which will be used to store network address, broadcast address, and subnet mask in dotted decimal form
        
        classfulNetworkAddress = []
        classfulBroadcastAddress = []
        classfulSubnetMaskDD = []

        #populate the lists with info from ipaddres, calculate the classful address based on subnet mask
        print("Classful Network Address: ", end = '')
        screenText += "Classful Network Address: "
        for x in ipAddress:
            classfulNetworkAddress.append(x)
            classfulBroadcastAddress.append(x)
            classfulSubnetMaskDD.append(x)

        if(subnetMask >= 24):
             classfulNetworkAddress[3] = 0
          
        elif(subnetMask >= 16):
             classfulNetworkAddress[2] = 0
             classfulNetworkAddress[3] = 0
          
        elif(subnetMask >= 8):
              classfulNetworkAddress[1] = 0
              classfulNetworkAddress[2] = 0
              classfulNetworkAddress[3] = 0

        #display the classful network address
        for x in range (0,3):
            print(str(classfulNetworkAddress[x])+'.')
            screenText += (str(classfulNetworkAddress[x])+'.')
        print(str(classfulNetworkAddress[3]))
        screenText += str(classfulNetworkAddress[3])

        #Calculate the classful broadcast address
        print ( "\nClassful Broadcast Address: ", end = '')
        screenText += "\nClassful Broadcast Address: "
        if(subnetMask >= 24):
             classfulBroadcastAddress[3] = 255
          
        elif(subnetMask >= 16):
            classfulBroadcastAddress[2] = 255
            classfulBroadcastAddress[3] = 255
          
        elif(subnetMask >= 8):
              classfulBroadcastAddress[1] = 255
              classfulBroadcastAddress[2] = 255
              classfulBroadcastAddress[3] = 255

        for x in range (0,3):
            print(str(classfulBroadcastAddress[x])+'.')
            screenText += (str(classfulBroadcastAddress[x])+'.')
        print(str(classfulBroadcastAddress[3]))
        screenText += (str(classfulBroadcastAddress[3]))

        #Display the classful subnet mask in dotted decimal notation
        print("\nClassful Subnet Mask in dotted decimal form: ", end = '')
        screenText += "\nClassful Subnet Mask in dotted decimal form: "

        if(subnetMask >= 24):
             classfulSubnetMaskDD[0] = 255
             classfulSubnetMaskDD[1] = 255
             classfulSubnetMaskDD[2] = 255
             classfulSubnetMaskDD[3] = 0

        elif(subnetMask >= 16):
             classfulSubnetMaskDD[0] = 255
             classfulSubnetMaskDD[1] = 255
             classfulSubnetMaskDD[2] = 0
             classfulSubnetMaskDD[3] = 0
          
        elif(subnetMask >= 8):
              classfulSubnetMaskDD[0] = 255
              classfulSubnetMaskDD[1] = 0
              classfulSubnetMaskDD[2] = 0
              classfulSubnetMaskDD[3] = 0

        for x in range (0,3):
            print(classfulSubnetMaskDD[x], end= '.')
            screenText += (str(classfulSubnetMaskDD[x])+'.')
        print(classfulSubnetMaskDD[3], end= '')
        screenText += str(classfulSubnetMaskDD[3])

        #Find the total number of usable hosts per subnet based on mask
        hostBitsC = 32 - subnetMask
        hostBitsB = 32 - subnetMask - 8
        hostBitsA = 32 - subnetMask - 16
        totalHostsPerSubnetC = pow (2, hostBitsC)
        totalHostsPerSubnetB = pow (2, hostBitsB)
        totalHostsPerSubnetA = pow (2, hostBitsA)
        usableHostsPerSubnet = int(totalHostsPerSubnetC - 2)

        print("\nNumber of usable hosts per subnet: ", usableHostsPerSubnet, end = '')
        screenText += ("\nNumber of usable hosts per subnet: " + str(usableHostsPerSubnet))

        #Display the class: A, B, or C
        print("\nClassful Network: " + nClass, end = '')
        screenText += ("\nClassful Network: " + str(nClass))

        #Calculate the subnet range
        validHost = True

        #if Class C, do the following
        if(subnetMask >= 24):
            evenDiv = int(ipAddress[3] / totalHostsPerSubnetC)
            netStart = evenDiv * totalHostsPerSubnetC
            subnetAddress[3] = netStart

            print("\nSubnet Network Address: ", end = '')
            screenText += ("\nSubnet Network Address: ")
            for x in range (0,3):
                print(subnetAddress[x], end = '.')
                screenText += (str(subnetAddress[x])+'.')
            print(subnetAddress[3], end = '')
            screenText += (str(subnetAddress[3]))

            #is it a validHost?
            if(subnetAddress[len(subnetAddress) -2] == ipAddress[-2]):
                validHost = False

            #Obtain first host in network
            firstHost = subnetAddress[3] + 1
            print ("\nHost range within subnet: ", end = '')
            screenText += ("\nHost range within subnet: ")
            for x in range (0,3):
                print(subnetAddress[x], end = '.')
                screenText += (str(subnetAddress[x])+'.')
            print(firstHost, end = '')
            screenText += (str(firstHost))
            print(" - ", end = '')
            screenText += (" - ")

            #Obtain subnet broadcast & last host in network
            subnetBroadcastAddress = subnetAddress[3] + totalHostsPerSubnetC -1
            lastHost = subnetAddress[3] + totalHostsPerSubnetC -2

            for x in range (0,3):
                print(subnetAddress[x], end = ".")
                screenText += (str(subnetAddress[x])+'.')
            print(lastHost)
            screenText += (str(lastHost))
            print("Subnet Broadcast Address: ", end = '')
            screenText += ("\nSubnet Broadcast Address: ")
            for x in range (0,3):
                print(subnetAddress[x], end = ".")
                screenText += (str(subnetAddress[x])+'.')
            
            #validHost?
            print(subnetBroadcastAddress)
            screenText += (str(subnetBroadcastAddress))
            if(subnetBroadcastAddress == ipAddress[len(subnetAddress) -2]):
                validHost = False

        #if Class B, do the following
        elif(subnetMask >= 16):
            evenDiv = int(ipAddress[2] / totalHostsPerSubnetB)
            netStart = evenDiv * totalHostsPerSubnetB
            subnetAddress[2] = netStart
            subnetAddress[3] = 0

            print("\nSubnet Network Address: ", end = '')
            screenText += ("\nSubnet Network Address: ")
            for x in range (0,3):
                print(subnetAddress[x], end = ".")
                screenText += (str(subnetAddress[x])+'.')
            print(subnetAddress[3], end = "")
            screenText += (str(subnetAddress[3]))

            #validHost Network Address check
            if(subnetAddress[len(subnetAddress) -2] == ipAddress[len(subnetAddress) -2]):
                validHost = False
            
            #Add one to this to get first Host
            firstHost = subnetAddress[3] + 1
            print("\nHost range within subnet: ", end ='')
            screenText += ("\nHost range within subnet: ")

            for x in range (0,3):
                print(subnetAddress[x], end =".")
                screenText += (str(subnetAddress[x])+'.')

            print(firstHost, end = " ")
            screenText += (str(firstHost)+" ")

            blockSize = subnetAddress[3] + totalHostsPerSubnetC
            octet3 = int((blockSize / 256) + subnetAddress[2] -1)
            octet4 = blockSize % 256
            if(octet4 == 0):
                octet4 = 255
            print("-", end = " ")
            screenText += ("- ")
            for x in range (0,2):
                print(subnetAddress[x], end = ".")
                screenText += (str(subnetAddress[x])+'.')
            print(octet3, end = ".")
            screenText += (str(octet3)+'.')
            print(octet4 - 1, end = "")
            screenText += (str(octet4-1))

            print("\nSubnet Broadcast Address: ", end ='')
            screenText += ("\nSubnet Broadcast Address: ")
            for x in range (0,2):
                print(subnetAddress[x], end = ".")
                screenText += (str(subnetAddress[x])+'.')
            print(octet3, end = ".")
            screenText += (str(octet3)+'.')
            print(octet4)
            screenText += (str(octet4))

        #ValidHost, make sure it isnt the broadcast address
            if(octet4 == ipAddress[len(subnetAddress)-2]):
                validHost = False
            
        #Class A
        elif(subnetMask >= 8):
            evenDiv = int(ipAddress[1] / totalHostsPerSubnetA)
            netStart = evenDiv * totalHostsPerSubnetA
            subnetAddress[1] = netStart
            subnetAddress[2] = 0
            subnetAddress[3] = 0

            print("\nSubnet Network Address: ", end ='')
            screenText += ("\nSubnet Network Address: ")
            for x in range(0,3):
                print(subnetAddress[x], end =".")
                screenText += (str(subnetAddress[x])+'.')
            print(subnetAddress[3], end ="")
            screenText += (str(subnetAddress[3]))

            #validHost Network address compare
            if(subnetAddress[len(subnetAddress)-2] == ipAddress[len(subnetAddress) -2]):
                validHost = False

            #First Host in network
            firstHost = subnetAddress[3] + 1
            print("\nHost range within subnet: ", end ='')
            screenText += ("\nHost range within subnet: ")
            for x in range (0,3):
                print(subnetAddress[x], end ='.')
                screenText += (str(subnetAddress[x])+'.')
            print(firstHost, end = '')
            screenText += (str(firstHost))
            print(" -", end = " ")
            screenText += (" - ")
           
            blockSize = subnetAddress[3] + totalHostsPerSubnetC
            octet3 = int((blockSize / 256) + subnetAddress[2] -1)
            octet2 = int(octet3 / 256 + subnetAddress[1])
            octet3 = 255
            octet4 = 255

            for x in range(0,1):
                print(subnetAddress[x], end='.')
                screenText += (str(subnetAddress[x])+'.')
            print(octet2, end = ".")
            screenText += (str(octet2)+'.')
            print(octet3, end = ".")
            screenText += (str(octet3)+'.')
            print(octet4 - 1, end =" ")
            screenText += (str(octet4-1)+" ")

            print("\nSubnet Broadcast Address: ", end = '')
            screenText += ("\nSubnet Broadcast Address: ")
            for x in range (0,1):
                print(subnetAddress[x], end = ".")
                screenText += (str(subnetAddress[x])+'.')

            print(octet2, end = ".")
            screenText += (str(octet2)+'.')
            print(octet3, end = ".")
            screenText += (str(octet3)+'.')
            print(octet4, end ="\n")
            screenText += (str(octet4))

            #Make sure the ipAddress isnt the broadcast address
            if(octet4 == ipAddress[len(subnetAddress) -2]):
                validHost = False

        # Valid host address
        
        print("\nClassful Subnet Mask:", classfulSubnetMask)
        screenText += ("\nClassful Subnet Mask: " + str(classfulSubnetMask))
        print("Is it a valid Host Address?: ", end='')
        screenText += ("\nIs it a valid Host Address?: ")
        if(validHost):
            print("Yes")
            screenText += ("Yes")
        else:
            print("No")
            screenText += ("No")
            
        self.mainView.setDisplayText(screenText)

                
    def _calculateResult(self):
        """Evaluate expressions."""
        result = self.evaluateProblem(expression=self.mainView.getDisplayText())
        self.mainView.setDisplayText(result)

    def _buildExpression(self, sub_exp):
        """Build expression."""
        if self.mainView.getDisplayText() == ERROR_MSG:
            self.mainView.clearDisplay()

        expression = self.mainView.getDisplayText() + sub_exp
        self.mainView.setDisplayText(expression)



# Create a Model to handle the calculator's operation
def evaluateProblem(expression):
    """Evaluate an expression."""
    try:
        result = str(eval(expression))
    except Exception:
        result = ERROR_MSG

    return result

# Client code
def main():
    """Main function."""
    # Create an instance of `QApplication`
    calcApp = QApplication(sys.argv)
    # Show the calculator's GUI
    mainView = calcGui()
    mainView.show()
    
    #p =  main.palette()
    #p.setColor(main.backgroundRole(), Qt.black)
    #main.setPalette(p)
    
    # Create instances of the model and the controller
    model = evaluateProblem
    CalcController(model=model, view=mainView)
    
    
    # Execute calculator's main loop
    sys.exit(calcApp.exec_())


if __name__ == "__main__":
    main()
