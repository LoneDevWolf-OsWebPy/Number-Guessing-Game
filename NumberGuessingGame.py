# ======================================================================================================================
#                                           Author: LoneDevWolf~☕🚀
# ======================================================================================================================
#                           Algorithm for Creating a Number Guessing Game and How it works
# ======================================================================================================================
# 1. User inputs he lower bound and upper bound of the range.
# 2. The compiler generates a random integer between the range and store it in a variable for future references.
# 3. For repetitive guessing, a while loop will be initialized.
# 4. If the user guessed a number which is greater than a randomly selected number, the user gets an output "Try Again!
#    Your guess is too high"
# 5. Else if the user guessed a number which is smaller than a randomly selected number, the user gets an output
#    "Try Again! You guessed too small"
# 6. And if the user guessed in a minimum number of guesses, the user get "Congratulations!" output
# 7. Else if the user didn't guess the integer in the minimum number of guesses, he/she will get a better luck next time
#    output.
# ======================================================================================================================
#                                                   Solutions 1
# ======================================================================================================================

# Import the random and maths modules
import random
import math

#
# # Taking Inputs
# lowerBound = int(input("Enter your Lower Bound:- "))
# upperBound = int(input("Enter your Upper Bound:- "))
#
# # Generating random number between the lower and upper bound
# randomNumbers = random.randint(lowerBound, upperBound)
# print("\n\tYou have only ", round(math.log(upperBound - lowerBound + 1, 2)), " chances to guess the integer! \n")
#
# # Initializing the number of guesses.
# guessCount = 0
#
# # For calculation of minimum number of guesses depends upon range
# while guessCount < math.log(upperBound - lowerBound + 1, 2):
#     guessCount += 1
#     # Taking guessing number as input
#     guess = int(input("Guess a number:- "))
#     guessTrial = 0
#     # Condition testing
#     if guess == guessTrial:
#         print("Congratulations you did it in ", guessCount, " try")
#         # Once  guessed right, loop will break
#         break
#     elif guess > guessTrial:
#         print("You guessed too small")
#     elif guess < guessTrial:
#         print("You guessed too high")
#         # If guessing is more than required guesses, then show this output
# if guessCount >= math.log(upperBound - lowerBound + 1, 2):
#     print("\nThe Number is %d" % guess)
#     print("\tBetter Luck Next time!")

# ======================================================================================================================
#                                                   Solutions 2
# ======================================================================================================================
# The flaws with this second program is that it has no guess limit
# num = random.randint(1, 10)
# guess = None
#
# while guess != num:
#     guess = int(input("Guess a number between 1 and 10:- "))
#
#     if guess == num:
#         print("Congratulations! you guessed right!!! ")
#         break
#     else:
#         print("Nope, Sorry, Try Again later.")

# ======================================================================================================================
#                                                   Solutions 3
# ======================================================================================================================
lowerBound = 1
upperBound = 1000
maxAttempts = 10

secretNumber = random.randint(lowerBound, upperBound)


# Read the User Input
def getGuess():
    while True:
        try:
            guess = int(input(f"Guess a number between {lowerBound} and {upperBound}:-  "))
            if lowerBound <= guess <= upperBound:
                return guess
            else:
                print("Invalid Input, Please enter number with range of 1 - 1000. ")
        except ValueError:
            print("Invalid Input. Please enter a valid number.")


# Validate the User Guess
def checkGuess(guess, secretnumber):
    if guess == secretnumber:
        return "Correct"
    elif guess < secretnumber:
        return "Too Low"
    else:
        return "Too High"


def playGame():
    attempts = 0
    won = False

    while attempts < maxAttempts:
        attempts += 1
        guess = getGuess()
        result = checkGuess(guess, secretNumber)

        if result == "Correct":
            print(f"Congratulations! You guessed the secret number {secretNumber} in {attempts} attempts.")
            won = True
            break
        else:
            print(f"{result}. Try Again!")

            if not won:
                print(f"Sorry, you ran out of Attempts. The secret number is {secretNumber}!. ")


if __name__ == "__main__":
    print("Welcome to the Number Guessing Game!")
    playGame()


# ======================================================================================================================
#                                             Have a Goodly Learning
#                                                 LoneDevWolf~☕🚀
# ======================================================================================================================
