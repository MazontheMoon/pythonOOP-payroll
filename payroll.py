# SD-TA-007 Excercise 3
# Author: Mary Ronan
# Payroll Application with Object-Orientated Python

import datetime

# Class
class Employee:

    # Class Variables
    company = "GRETB"
    taxRate = 0.2

    # Class Instance Variables
    def __init__(self, empNo, empName, hoursWorked, rateOfPay):
        self.empNo = empNo
        self.empName = empName
        self.hoursWorked = hoursWorked
        self.rateOfPay = rateOfPay
        self.grossPay = 0.0
        self.nettPay = 0.0

    # Greet User
    def welcomeMessage():
        print("=".ljust(70, "="))
        print(Employee.company.center(70))
        print("Welcome to your Payroll Application".center(70))
        print("=".ljust(70, "="))          

    # Exit Message
    def exitMessage():
        print("=".ljust(70, "="))
        print("Thank you for using Payroll Application".center(70))
        print("=".ljust(70, "="))

    # Calculate Gross Pay
    def calcGross(self):
        self.grossPay = self.hoursWorked * self.rateOfPay
        return self.grossPay

    # Calculate Nett Pay
    def calcNettPay(self):
        self.nettPay = self.grossPay - (self.grossPay * self.taxRate)
        return self.nettPay

    # Display Payslip
    def printPayslip(self):
        timeStamp = datetime.datetime.now().strftime("%c")
        print("-".ljust(70, "-"))
        print(f"Employee Payslip: {self.empName}".center(70))
        print(timeStamp.center(70))
        print("-".ljust(70, "-"))
        print("Employee Number".ljust(20),":", self.empNo)
        print("Employee Name".ljust(20),":", self.empName)
        print("Hours Worked".ljust(20),":", self.hoursWorked)
        print("Rate of Pay".ljust(20),": €", self.rateOfPay)
        print("Gross Pay".ljust(20),": €", self.calcGross())
        print("Nett Pay".ljust(20),": €", self.calcNettPay())
        print("-".ljust(70, "-"))

# Validate Input
def getValidStringInput(message):
    while(True):
        try:
            value = input(message)
            if value == "" :
                raise Exception
            else:
                return value
        except:
            print("Invalid Entry, please try again. \n")

def getValidIntInput(message):
    while(True):
        try:
            value = int((input(message)))
            if value < 0 :
                raise Exception
            else:
                return value
        except:
            print("Invalid Entry, please try again. \n")

def getValidFloatInput(message):
    while(True):
        try:
            value = float((input(message)))
            if value < 0.0 :
                raise Exception
            else:
                return value
        except:
            print("Invalid Entry, please try again. \n")

# Main Program        
def main():

    # Greet user
    Employee.welcomeMessage()

    # Get user values
    empNo = getValidStringInput("Enter Employee Number: ")
    empName = getValidStringInput("Enter Employee Name: ")
    hoursWorked = getValidIntInput("Enter Number of Hours Worked: ")
    rateOfPay = getValidFloatInput("Enter Pay Rate: €")

    # Create employee object
    myEmployee = Employee(empNo, empName, hoursWorked, rateOfPay)    

    # Display payslip
    myEmployee.printPayslip()

    # Display exit message
    Employee.exitMessage()

main()
