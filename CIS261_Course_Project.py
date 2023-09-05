from datetime import datetime

def CreateUsers():
    print("Create users, passwords, and roles:")
    UserFile = open("Users.txt", "a+")
    while True:
        username = GetUserName()
        if (username.upper() == "END"):
            break
        userpwd = GetUserPassword()
        userrole = GetUserRole()
        
        UserDetail = username + "|" + userpwd + "|" + userrole + "\n"
        UserFile.write(UserDetail)
        
    UserFile.close()
    printuserinfo()
    
def GetUserName():
    username = input("Enter username or 'End' to quit: ")
    return username

def GetUserPassword():
    pwd = input("Enter password ")
    return pwd


def GetUserRole():
    userrole = input("Enter role (Admin  or user): ")
    while True:
        if (userrole.upper() == "ADMIN" or userrole.upper() == "USER"):
            return userrole
        else:
            userrole = input("Enter role (Admin or User): ")
            
def printuserinfo():
    UserFile = open("Users.txt", "r")
    while True:
        UserDetail = UserFile.readline()
        if not UserDetail:
            break
        UserDetail = UserDetail.replace("\n", "")
        UserList = UserDetail.split("|")
        username = UserList[0]
        userpassword = UserList[1]
        userrole = UserList[2]
        print("User name: ", username, "Password: ", userpassword, "Role: ", userrole)


def Login():
    UserFile = open("Users.txt", "r")
    UserList = []
    UserName = input("Enter user name: ")
    UserPwd = input("Enter user password: ")
    UserRole = "None"
    while True:
        UserDetail = UserFile.readline()
        if not UserDetail:
            return UserRole, UserName, UserPwd
        UserDetail = UserDetail.replace("\n", "")
      
        UserList = UserDetail.split("|")
        if UserName == UserList[0] and UserPwd == UserList[1]:
           UserRole = UserList[2]
           return UserRole, UserName
    return UserRole, UserName
           
            

def get_date_range():
    fromdate = input("Enter the start date (mm/dd/yyyy): ")
    todate = input("Enter the end date (mm/dd/yyyy): ")
    return fromdate, todate

def get_employee_name():
    employee_name = input("Enter Employee Name: ")
    return employee_name

def get_total_hours():
    while True:
        try:
            hours = float(input("Enter total hours worked:  "))
            return hours
        except ValueError:
            print("Invalid input. Please enter a valid number for hours.")
def get_hourly_rate():
    while True:
        try:
            rate = float(input("Enter hourly rate:  "))
            return rate
        except ValueError:
            print("Invalid input. Please enter a valid number for the hourly rate.")
def get_income_tax_rate():
    while True:
        try:
            tax_rate = float(input("Enter income tax rate:  "))
            return tax_rate
        except ValueError:
            print("Invalid input. please enter a valid number for the income tax rate.")

def calculate_pay(total_hours, hourly_rate, tax_rate):
    gross_pay = total_hours * hourly_rate
    income_tax = gross_pay * (tax_rate / 100)
    net_pay = gross_pay - income_tax
    return gross_pay, income_tax, net_pay

def printInfo(empDetailList):
    total_employees = 0
    total_hours = 0.00
    total_gross_pay = 0.00
    total_tax = 0.00
    total_net_pay = 0.00
    for emplist in empDetailList:
        fromdate = emplist[0]
        todate = emplist[1]
        employee_name = emplist[2]
        hours = emplist[3]
        rate = emplist[4]
        tax_rate = emplist[5]
        
        gross_pay, income_tax, net_pay = calculate_pay(hours, rate, tax_rate)
        print(fromdate, todate, employee_name, f"{hours:,.2f}", f"{rate:,.2f}", f"{gross_pay:,.2f}", f"{tax_rate:,.1%}", f"{income_tax:,.2f}", f"{net_pay:,.2f}")
        
        total_employees += 1
        total_hours += 1
        total_gross_pay = gross_pay
        total_tax += income_tax
        total_net_pay += net_pay
        
    empTotals["totEmp"] = total_employees
    empTotals["totHours"] = total_hours
    empTotals["totGross"] = total_gross_pay
    empTotals["totTax"] = total_tax
    empTotals["totNet"] = total_net_pay
        

def printTotals(empTotals):
    print()
    print(f"Total Number of Employees: {empTotals['totEmp']}")
    print(f"Total hours of the Employee: {empTotals['totHours']}")
    print(f"Total Gross Pay of the Employee: {empTotals['totGross']:,.2f}")
    print(f"Total tax of Employee: {empTotals['totTax']:,.1%}")
    print(f"Total net pay of Employee: {empTotals['totNet']:,.2f}")
    
def WriteEmployeeInformation(employee):
    file = open("employeeinfo.txt", "a")
    file.write('{}|{}|{}|{}|{}|{}\n'.format(employee[0], employee[1], employee[2], employee[3], employee[4], employee[5]))
    
def GetFromDate():
    valid = False
    fromdate = ""
    
    while not valid:
        fromdate = input("Enter from date (mm/dd/yyyy): ")
        if (len(fromdate.split('/')) != 3 and fromdate.upper() != 'ALL'):
            print("Invalid date format")
        else:
            valid = True
        
    return fromdate

def ReadEmployeeInformation(fromdate):
    empDetailList = []
    
    file = open("employeeinfo.txt", "r")
    data = file.readlines()
    
    condition = True
    
    if fromdate.upper() == 'ALL':
        condition = False
        
    for employee in data:
        employee = [x.strip() for x in employee.strip().split("|")]
        
        if not condition:
            empDetailList.append([employee[0], employee[1], employee[2], float(employee[3]), float(employee[4]), float(employee[5])])
        else:
            if fromdate == employee[0]:
                empDetailList.append([employee[0], employee[1], employee[2], float(employee[3]), float(employee[4]), float(employee[5])])
    return empDetailList


if __name__ == "__main__":
    CreateUsers()
    print()
    print("Data Entry")
    UserRole, UserName = Login()
    DetailsPrinted = False
    empDetailList = []
    empTotals = {}
    if (UserRole.upper() == "NONE"):
        print(UserName, " is Invalid")
    else:
        if (UserRole.upper() == "ADMIN"):
            EmpFile = open("employee.txt", "a+")
    
    while True:
        employee_name = get_employee_name()
        if (employee_name.upper() == "END"):
            break
        fromdate, todate = get_date_range()
        hours = get_total_hours()
        rate = get_hourly_rate()
        tax_rate = get_income_tax_rate()
        
        print()
        
        empDetail = [fromdate, todate, employee_name, hours, rate, tax_rate]
        WriteEmployeeInformation(empDetail)
    print()
    print()
    fromdate = GetFromDate()
    
    empDetailList = ReadEmployeeInformation(fromdate)
    
    print()
    printInfo(empDetailList)
    print()
    printTotals(empTotals)
       