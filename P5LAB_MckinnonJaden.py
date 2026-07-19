# Jaden McKinnon
# July 19, 2026
# P5LAB
# This program simulates a self-checkout machine by generating a random
# purchase total, accepting a cash payment from the user, calculating
# the change owed, and displaying the number of dollars, quarters,
# dimes, nickels, and pennies to return.

import random


def disperse_change(change):
    # Convert change to pennies
    change = round(change * 100)

    dollars = change // 100
    change = change % 100

    quarters = change // 25
    change = change % 25

    dimes = change // 10
    change = change % 10

    nickels = change // 5
    change = change % 5

    pennies = change

    # Display the change
    if dollars > 0:
        print(dollars, "Dollar(s)")
    if quarters > 0:
        print(quarters, "Quarter(s)")
    if dimes > 0:
        print(dimes, "Dime(s)")
    if nickels > 0:
        print(nickels, "Nickel(s)")
    if pennies > 0:
        print(pennies, "Pennie(s)")

    if dollars == 0 and quarters == 0 and dimes == 0 and nickels == 0 and pennies == 0:
        print("No change")


def main():
    # Generate a random purchase total
    amount_owed = round(random.uniform(0.01, 100.00), 2)

    print(f"You owe: ${amount_owed:.2f}")

    # Get payment from the user
    cash = float(input("How much cash will you put in the self-checkout? $"))

    # Calculate change
    change = round(cash - amount_owed, 2)

    print(f"Change is: ${change:.2f}")

    # Display the change
    disperse_change(change)


# Call the main function
main()