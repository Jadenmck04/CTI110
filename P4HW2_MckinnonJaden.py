# Jaden Mckinnon
# July 5, 2026
# P4HW2
# This program calculates payroll for multiple employees
# and displays payroll totals when the user enters "Done".

# Initialize totals
total_overtime = 0
total_regular = 0
total_gross = 0
employee_count = 0

# Get first employee name
employee_name = input("Enter employee's name or Done to terminate: ")

while employee_name.lower() != "done":

    hours = float(input("How many hours did " + employee_name + " work? "))
    pay_rate = float(input("What is " + employee_name + "'s pay rate? "))

    # Calculate pay
    if hours > 40:
        overtime_hours = hours - 40
        regular_hours = 40
    else:
        overtime_hours = 0
        regular_hours = hours

    overtime_pay = overtime_hours * (pay_rate * 1.5)
    regular_pay = regular_hours * pay_rate
    gross_pay = regular_pay + overtime_pay

    # Display employee information
    print("---------------------------------------")
    print("Employee Name:", employee_name)
    print("---------------------------------------")
    print(f"{'Hours Worked':<15}{'Pay Rate':<12}{'OverTime':<12}{'OverTime Pay':<15}{'RegHour Pay':<15}{'Gross Pay'}")
    print(f"{hours:<15.2f}{pay_rate:<12.2f}{overtime_hours:<12.2f}{overtime_pay:<15.2f}{regular_pay:<15.2f}{gross_pay:.2f}")
    print()

    # Update totals
    total_overtime += overtime_pay
    total_regular += regular_pay
    total_gross += gross_pay
    employee_count += 1

    # Ask for next employee
    employee_name = input("Enter employee's name or Done to terminate: ")

# Display totals
print("\nTotal number of employees entered:", employee_count)
print(f"Total amount paid for overtime: ${total_overtime:.2f}")
print(f"Total amount paid for regular hours: ${total_regular:.2f}")
print(f"Total amount paid in gross: ${total_gross:.2f}")