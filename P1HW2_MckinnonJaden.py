# Jaden McKinnon
# June 14, 2026
# P1HW2 - Travel Budget
# This program calculates travel expenses and remaining budget.

# Pseudocode:
# 1. Ask the user for their budget.
# 2. Ask for their travel destination.
# 3. Ask for gas expenses.
# 4. Ask for accommodation expenses.
# 5. Ask for food expenses.
# 6. Add all expenses together.
# 7. Subtract expenses from the budget.
# 8. Display the destination, budget, expenses, and remaining balance.

budget = float(input("Enter Budget: "))
destination = input("Enter your travel destination: ")
gas = float(input("How much do you think you will spend on gas? "))
hotel = float(input("Approximately, how much will you need for accommodation/hotel? "))
food = float(input("Last, how much do you need for food? "))

expenses = gas + hotel + food
remaining = budget - expenses

print("\n------------Travel Expenses------------")
print("Location:", destination)
print("Initial Budget:", budget)

print("\nFuel:", gas)
print("Accommodation:", hotel)
print("Food:", food)

print("\nRemaining Balance:", remaining)