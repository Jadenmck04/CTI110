import random

def play_game():
    number = random.randint(1, 100)
    guesses = 0

    print("\nI'm thinking of a number between 1 and 100.")

    while True:
        try:
            guess = int(input("Enter your guess: "))
            guesses += 1

            if guess < number:
                print("Too low!")
            elif guess > number:
                print("Too high!")
            else:
                print(f"Correct! You guessed the number in {guesses} guesses.")
                break
        except ValueError:
            print("Please enter a valid number.")

print("Welcome to the Number Guessing Game!")

while True:
    play_game()

    again = input("\nWould you like to play again? (yes/no): ").lower()

    if again != "yes":
        print("Thanks for playing!")
        break