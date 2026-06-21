# Jaden McKinnon
# 06/21/2026
# P2HW2_JadenMcKinnon
# This program collects six module grades, stores them in a list,
# and displays the lowest grade, highest grade, sum, and average.

"""
Pseudocode:

1. Create an empty list named module_grades.
2. Ask the user to enter the grade for Module 1.
3. Ask the user to enter the grade for Module 2.
4. Ask the user to enter the grade for Module 3.
5. Ask the user to enter the grade for Module 4.
6. Ask the user to enter the grade for Module 5.
7. Ask the user to enter the grade for Module 6.
8. Store each grade in the module_grades list.
9. Find the lowest grade using min().
10. Find the highest grade using max().
11. Find the sum of all grades using sum().
12. Find the average by dividing the sum by the number of grades.
13. Display the results with proper formatting.
"""

# Create list and collect grades
module_grades = []

module_grades.append(float(input("Enter grade for Module 1: ")))
module_grades.append(float(input("Enter grade for Module 2: ")))
module_grades.append(float(input("Enter grade for Module 3: ")))
module_grades.append(float(input("Enter grade for Module 4: ")))
module_grades.append(float(input("Enter grade for Module 5: ")))
module_grades.append(float(input("Enter grade for Module 6: ")))

# Calculations
lowest_grade = min(module_grades)
highest_grade = max(module_grades)
grade_sum = sum(module_grades)
grade_average = grade_sum / len(module_grades)

# Display results
print("\n------------Results------------")
print(f"Lowest Grade:      {lowest_grade}")
print(f"Highest Grade:     {highest_grade}")
print(f"Sum of Grades:     {grade_sum}")
print(f"Average:           {grade_average:.2f}")
print("--------------------------------")