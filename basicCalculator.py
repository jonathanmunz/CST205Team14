#Jonathan Munz, David Ruiz, Monica Barrios, Weixuan Jia
#Final.py
#Group 14
#Professor Modes
#This program will function as a calculator
#Ask the user what type of calculator they would like to use
# 1) Basic, 2) Scienctific, 3) Graphing, 4) Subnet
SelectionCalc = input('What type of calculator would you like to use today? 1) Basic, 2) Scienctific, 3) Graphing, 4) Subnet\n')
if (SelectionCalc == '1'):
    print('You have chosen Basic: ')
    #1) Basic
    #Ask the user which operation they would like to perform
    #1) Add, 2) Subtract, 3) Multiply, 4) Divide
    SelectionBasic = input('What operation would you like to perform? 1) Addition, 2) Subtration, 3) Multiplication, 4) Division\n')
    if (SelectionBasic == '1'):
        print('You have chosen addition')
        print('Please enter the two number you would like to add: ')
        x = int(input('Your first number: '))
        y = int(input('Your second number: '))
        a = x + y
        print(a)
    elif (SelectionBasic == '2'):
        print('You have chosen subtration')
        print('Please enter the two number you would like to subtract: ')
        x = int(input('Your first number: '))
        y = int(input('Your second number: '))
        a = x - y
        print(a)
    elif (SelectionBasic == '3'):
        print('You have chosen multiplication')
        print('Please enter the two number you would like to multiply: ')
        x = int(input('Your first number: '))
        y = int(input('Your second number: '))
        a = x * y
        print(a)
    elif (SelectionBasic == '4'):
        print('You have chosen division')
        print('Please enter the two number you would like to divide: ')
        x = int(input('Your first number: '))
        y = int(input('Your second number: '))
        a = x / y
        print(a)
elif (SelectionCalc == '2'):
    print('You have chosen Scientific: ')
elif (SelectionCalc == '3'):
    print('You have chosen Graphing: ')
elif (SelectionCalc == '4'):
    print('You have chosen Subnet: ')