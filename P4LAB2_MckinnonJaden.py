run_again = "yes"

while run_again.lower() == "yes":

    number = int(input("Enter an integer: "))

    if number >= 0:
        print("\nMultiplication Table for", number)

        for i in range(1, 13):
            print(f"{number} x {i} = {number * i}")

    else:
        print("Sorry, I cannot accept negative values.")

    run_again = input("\nWould you like to run the program again? (yes/no): ")

print("Program ended.")