# Jaden McKinnon
# 06/28/2026
# P3HW2 - Salary
# This program calculates an employee's regular pay,
# overtime pay, and gross pay based on hours worked.

# PSEUDOCODE
# 1. Ask the user for employee name.
# 2. Ask the user for hours worked.
# 3. Ask the user for pay rate.
# 4. If hours worked is greater than 40:
#       Calculate overtime hours.
#       Calculate overtime pay at 1.5 times pay rate.
#       Calculate regular pay for 40 hours.
#    Else:
#       Set overtime hours and overtime pay to 0.
#       Calculate regular pay for all hours worked.
# 5. Calculate gross pay.
# 6. Display employee information and pay details.

# Get employee information
employee_name = input("Enter employee's name: ")
hours_worked = float(input("Enter number of hours worked: "))
pay_rate = float(input("Enter employee's pay rate: "))

# Calculate pay
if hours_worked > 40:
    overtime_hours = hours_worked - 40
    regular_hours = 40
    overtime_pay = overtime_hours * (pay_rate * 1.5)
else:
    overtime_hours = 0
    regular_hours = hours_worked
    overtime_pay = 0

regular_pay = regular_hours * pay_rate
gross_pay = regular_pay + overtime_pay

# Display results
print("\n----------------------------------------")
print("Employee Name:", employee_name)
print("----------------------------------------")
print(f"{'Pay Rate:':20}${pay_rate:.2f}")
print(f"{'Hours Worked:':20}{hours_worked:.1f}")
print(f"{'Overtime Hours:':20}{overtime_hours:.1f}")
print(f"{'Overtime Pay:':20}${overtime_pay:.2f}")
print(f"{'Regular Pay:':20}${regular_pay:.2f}")
print(f"{'Gross Pay:':20}${gross_pay:.2f}")