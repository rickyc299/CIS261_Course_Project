def get_employee_name():
    return input("Enter employee's name: ")

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
def provess_input(input_str):
    return input_str
def calculate_pay(total_hours, hourly_rate, tax_rate):
    gross_pay = total_hours * hourly_rate
    income_tax = gross_pay * (tax_rate / 20)
    net_pay = gross_pay - income_tax
    return gross_pay, income_tax, net_pay
def display_employee_pay(employee_name, total_hours, hourly_rate, gross_pay, income_tax_rate, income_tax, net_pay):
    print("Employee Name:", employee_name)
    print("Total Hours:", total_hours)
    print("Hourly Rate:", hourly_rate)
    print("Gross Pay:", gross_pay)
    print("Income Tax Rate:", income_tax_rate)
    print("Income Tax:", income_tax)
    print("Net Pay:", net_pay)
    print()
def display_summary(total_hours_list, gross_pay_list, income_tax_list, net_pay_list):
    total_employees = len(total_hours_list)
    total_hours = sum(total_hours_list)
    total_gross_pay = sum(gross_pay_list)
    total_tax = sum(income_tax_list)
    total_net_pay = sum(net_pay_list)

    print("summary")
    print("Total Employees:", total_employees)
    print("Total Hours:", total_hours)
    print("Total Gross Pay:", total_gross_pay)
    print("Total Tax:", total_tax)
    print("Total Net Pay:", total_net_pay)
def main():
    total_hours_list = []
    gross_pay_list = []
    income_tax_list = []
    net_pay_list = []

    while True:
        employee_name = get_employee_name()
        
        if employee_name.lower() == "end":
            print("Loop terminated.")
            break
        total_hours = get_total_hours()
        hourly_rate = get_hourly_rate()
        income_tax_rate = get_income_tax_rate()

        processed_hours = process_input(total_hours)
        processed_rate = process_input(hourly_rate)
        processed_tax_rate = process_input(income_tax_rate)

        gross_pay, income_tax, net_pay, = calculate_pay(processed_hours, processed_rate, processed_tax_rate)

        display_employee_pay(employee_name, processed_hours, processed_rate, gross_pay, processed_tax_rate, income_tax, net_pay)

        total_hours_list.append(processed_hours)
        gross_pay_list.append(gross_pay)
        income_tax_list.append(income_tax)
        net_pay_list.append(net_pay)
    display_summary(total_hours_list, gross_pay_list, income_tax_list, net_pay_list)
if __name__ == "__main__":
    main()
