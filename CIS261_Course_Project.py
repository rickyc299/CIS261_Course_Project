def get_date_range():
    from_date = input("Enter the 'from' date (mm/dd/yyyy): ")
    to_date = input("Enter the 'to' date (mm/dd/yyyy): ")
    return from_date, to_date

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
    total_employee = 0
    total_hours = 0.00
    total_gross_pay = 0.00
    total_tax = 0.00
    total_net_pay = 0.00
    for emplist in empDetailList:
        from_date = emplist[0]
        to_date = emplist[1]
        employee_name = emplist[2]
        hours = emplist[3]
        rate = emplist[4]
        tax_rate = emplist[5]
        
        gross_pay, income_tax, net_pay = calculate_pay(hours, rate, tax_rate)
        print(from_date, to_date, employee_name, f"{hours:,.2f}", f"{rate:,.2f}", f"{gross_pay:,.2f}", f"{tax_rate:,.1%}", f"{income_tax:,.2f}", f"{net_pay:,.2f}")
        total_employee += 1
        total_hours += 1
        total_gross_pay = gross_pay
        total_tax += income_tax
        total_net_pay += net_pay
        
        empTotals["totEmp"] = total_employee
        empTotals["totHours"] = total_hours
        empTotals["totGross"] = total_gross_pay
        empTotals["totTax"] = total_tax
        empTotals["totNet"] = total_net_pay
        

def printTotals(empTotals):
    print(f'Total Number of Employees: {empTotals["totEmp"]}')
    print(f'Total hours of the Employee: {empTotals["totHours"]}')
    print(f'Total Gross Pay of the Employee: {empTotals["totGross"]}')
    print(f'Total tax of Employee: {empTotals["totTax"]}')
    print(f'Total net pay of Employee: {empTotals["totNet"]}')
                                                        
if __name__ == "__main__":
    empDetailList = []
    empTotals = []
    while True:
        employee_name = get_employee_name()
        
        if (employee_name.lower() == "end"):
            break
        from_date, to_date = get_date_range()
        hours = get_total_hours()
        rate = get_hourly_rate()
        tax_rate = get_income_tax_rate()
        empDetail = []
        empDetail.insert(0, from_date)
        empDetail.insert(1, to_date)
        empDetail.insert(2, employee_name)
        empDetail.insert(3, hours)
        empDetail.insert(4, rate)
        empDetail.insert(5, tax_rate)
        empDetailList.append(empDetail)
    printInfo(empDetailList)
    printTotals(empTotals)