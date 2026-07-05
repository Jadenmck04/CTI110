# Jaden Mckinnon
# July 5, 2026
# P4HW1
# This program collects test scores, validates the input,
# drops the lowest score, calculates the average,
# and displays the corresponding letter grade.

"""
Pseudocode

1. Ask the user how many scores they want to enter.
2. Create an empty list to store the scores.
3. Repeat for the number of scores:
    a. Ask the user for a score.
    b. While the score is less than 0 or greater than 100:
        - Display an error message.
        - Ask for a valid score.
    c. Add the valid score to the list.
4. Find the lowest score.
5. Remove the lowest score from the list.
6. Calculate the average of the remaining scores.
7. Determine the letter grade:
    - A = 90-100
    - B = 80-89
    - C = 70-79
    - D = 60-69
    - F = Below 60
8. Display:
    - Lowest score
    - Modified score list
    - Average
    - Letter grade
"""

# Ask how many scores
num_scores = int(input("How many scores do you want to enter? "))

# Create list
score_list = []

# Collect scores
for i in range(num_scores):

    score = float(input(f"Enter score #{i + 1}: "))

    while score < 0 or score > 100:
        print("\nINVALID Score entered!!!!")
        print("Score should be between 0 and 100.")
        score = float(input(f"Enter score #{i + 1} again: "))

    score_list.append(score)

# Find and remove the lowest score
lowest_score = min(score_list)
score_list.remove(lowest_score)

# Calculate average
average = sum(score_list) / len(score_list)

# Determine letter grade
if average >= 90:
    grade = "A"
elif average >= 80:
    grade = "B"
elif average >= 70:
    grade = "C"
elif average >= 60:
    grade = "D"
else:
    grade = "F"

# Display results
print("\n------------Results------------")
print(f"Lowest Score  : {lowest_score}")
print(f"Modified List : {score_list}")
print(f"Scores Average: {average:.2f}")
print(f"Grade         : {grade}")
print("--------------------------------")