# Classical game with two improvement. Guess the number in Python + Define the range + Define the number of guesses
import random

endNumber = input("Please, introduce a end number in order to know until what number you want to play")
secretNumber = random.randint(1, int(endNumber))

# Ask the player
numberGuesses = input("Please, introduce how many games do you want to play")
for guessesTaken in range(1, int(numberGuesses)):
    print("Take a guess.")
    guess = int(input())

    if guess < secretNumber:
        print("Your guess is too low")
    elif guess > secretNumber:
        print("Your guess is to high")
    else:
         break

if guess == secretNumber:
    print("Great! Congratulations" + "Your number is correct " + str(guess) + " is the number I wrote down")
else:
    print("No, the number I was thinking of was " + str(secretNumber))


