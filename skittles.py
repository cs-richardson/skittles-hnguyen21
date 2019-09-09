'''
This code generates a random number from 0 to 1023. If the user fails to guess
correctly, the code will say "Nope! There are way more Skittles than that. Guess again."
or "Nope! There are fewer Skittles than that. Guess again." if the user guesses
too low or high respectively. If they guess correctly, then the code will say
"That's right! Nom nom nom." and terminate.

By: Ben
'''

import random
skittles = random.randint(0, 1023)

numOfGuesses = 0

guess = int(input("O hai! I'm thinking of a number between 0 and 1023. What is it? "))

while guess != skittles:
    numOfGuesses = numOfGuesses + 1

    if guess < skittles:
        guess = int(input("Nope! There are way more Skittles than that. Guess again. "))
        
    else:
        guess = int(input("Nope! There are fewer Skittles than that. Guess again. "))

print("That's right! Nom nom nom.")
print("You guessed {} times!".format(numOfGuesses + 1))
        
