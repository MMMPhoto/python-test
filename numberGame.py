# Guess the number game
import random
import sys

# Ask player for name
print('Hello, what is your name?')
name = input()

# Explain the game
print(f'Well, {name}, I am thinking of a number between 1 and 20.')

# Assign random number
number = random.randint(1, 20)

# Give player 6 guesses
for num in range(6):
    print('Take a guess.')
    guess = input()

    if int(guess) == int(number):
        print(f'Good job, {name}! You guessed the number in {num + 1} tries')
        break
    elif int(guess) > int(number):
        print('Your guess is too high.')
        continue
    elif int(guess) < int(number):
        print('Your guess is too low.')
        continue