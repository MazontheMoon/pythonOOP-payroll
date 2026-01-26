'''
SD-GAL-05 SD-TA-007 Exercise 009
Author: Mary Ronan
Last Modified: 26/01/2026
Payroll Application with Object-Orientated Python and Unit Testing
'''

# Required Imports
import datetime
import unittest

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

# Class
class Manager(Employee):

    # Class Variables
    bonus = 100.00

    # Class Instance Variables
    def __init__(self, empNo, empName, hoursWorked, rateOfPay):
        super().__init__(empNo, empName, hoursWorked, rateOfPay)

    # Calculate Gross Pay
    def calcGross(self):
        self.grossPay = self.hoursWorked * self.rateOfPay
        self.grossPay = self.grossPay + self.bonus
        return self.grossPay

# Input Validation
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

# Greet user
Employee.welcomeMessage()

# Get user values
empNo = getValidStringInput("Enter Employee Number: ")
empName = getValidStringInput("Enter Employee Name: ")
hoursWorked = getValidIntInput("Enter Number of Hours Worked: ")
rateOfPay = getValidFloatInput("Enter Pay Rate: €")
empType = getValidStringInput("Enter Employee Type [E/M]: ")

# Display payslip
if empType.upper() == "E":
    employee = Employee(empNo, empName, hoursWorked, rateOfPay)
    employee.printPayslip()
else:
    manager = Manager(empNo, empName, hoursWorked, rateOfPay)
    manager.printPayslip()

# Display exit message
Employee.exitMessage()

# Unit Testing
class unittests(unittest.TestCase):

    # Test 001 - Employee Number contains more than 1 character
    def test001(self):
        assert (len(empNo) > 1)

    # Test 002 - Hours worked is NOT a negative value
    def test002(self):
        self.assertTrue(hoursWorked >= 0)

    # Test 003 - Employee object is member of Employee class
    def test003(self):
        if empType.upper() == "E":
            self.assertIsInstance(employee, Employee)
        if empType.upper() == "M":
            self.assertIsInstance(manager, Manager)

    # Test 004 - Gross Pay calculations correct

    def test004(self):
        if empType.upper() == "E":
            self.assertEqual(employee.calcGross(), hoursWorked * rateOfPay)
        if empType.upper() == "M":
            self.assertEqual(manager.calcGross(), hoursWorked * rateOfPay)
            
    # Test 005 - Bonus added to manager pay
    def test005(self):
        emp = Employee(empNo, empName, hoursWorked, rateOfPay)
        man = Manager(empNo, empName, hoursWorked, rateOfPay) 
        self.assertEqual(emp.calcGross(), man.calcGross() - 100.00)

unittest.main()
