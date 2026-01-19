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
        self.grossPay = 0.00
        self.nettPay = 0.00

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
        print("Payslip".ljust(20),":", self.empName)
        print("Employee Number".ljust(20),":", self.empNo)
        print("Employee Name".ljust(20),":", self.empName)
        print("Hours Worked".ljust(20),":", self.hoursWorked)
        print("Rate of Pay".ljust(20),": €", self.rateOfPay)
        print("Gross Pay".ljust(20),": €", self.calcGross())
        print("Nett Pay".ljust(20),": €", self.calcNettPay())
        print("Pay Period".ljust(20),":", timeStamp)
        print("-".ljust(70, "-"))

# Validate Input
def getValidTextInput():
    pass

def getValidNumberInput():
    pass

# Main Program        
def main():

    # Greet user
    Employee.welcomeMessage()

    # Get user values
    empNo = input("Enter Employee Number: ")
    empName = input("Enter Employee Name: ")
    hoursWorked = int(input("Enter Number of Hours Worked: "))
    rateOfPay = int(input("Enter Pay Rate: €"))

    # Create employee object
    myEmployee = Employee(empNo, empName, hoursWorked, rateOfPay)    

    # Display payslip
    myEmployee.printPayslip()

    # Display exit message
    Employee.exitMessage()

main()
