# A short program to guess the number, from "Automate the Boring Stuff With Python, 2nd Edition"

import random

# The following commented block of code is what I came up with before look at the book,
# based entirely in the book's example output, and without knowing the full features.
# This version allows infinite guesses. The book's implementation was to allow 6 guesses.
# Also, I wasn't paying close attention; the book's game is between 1 and 20, mine is between 1 and 100
# My code could probably be cleaner, but as a first attempt while still unfamiliar with Python,
# it does function. :)
#
#number = random.randint(1, 100)
#correct = False
#guesscount = 1
#
#print('I am thinking of a number between 1 and 100.')
#
#while not correct:
#    print('Take a guess.')
#    guess = int(input())
#    if guess == number:
#        print('Good job! You guessed my number in ' + str(guesscount) + ' guesses!')
#        correct = True
#    elif guess < number:
#        print('Your guess is too low.')
#        guesscount += 1
#    else:
#        print('Your guess is too high.')
#        guesscount += 1

# Below is the book's version as shown on page 50. I've already imported random up at the top of the file

secretNumber = random.randint(1, 20)
print('I am thinking of a number between 1 and 20.')

# Ask the player to guess 6 times
for guessesTaken in range(1, 7):
    print('Take a guess.')
    guess = int(input())

    if guess < secretNumber:
        print('Your guess is too low.')
    elif guess > secretNumber:
        print('Your guess is too high.')
    else:
        break # This condition is the correct guess!

# Give feedback based on whether or not the player managed to guess the correct number
if guess == secretNumber:
    print('Good job! You guessed my number in ' + str(guessesTaken) + ' guesses!')
else:
    print('Nope. The number I was thinking of was ' + str(secretNumber) + '.')


