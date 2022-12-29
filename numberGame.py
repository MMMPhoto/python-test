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
    guess = 0
    print(f'number of guesses: {num}')

    # Input validation
    while int(guess) < 1 or int(guess) > 20:
        guess = input()
        if int(guess) < 1 or int(guess) > 20:
            print('You must enter an integer between 1 and 20.')

    if int(guess) == int(number):
        print(f'Good job, {name}! You guessed the number in {num + 1} tries')
        break
    elif int(guess) > int(number):
        print('Your guess is too high.')
        continue
    elif int(guess) < int(number):
        print('Your guess is too low.')
        continue

# After player runs out of tries
print(f"Too bad! You couldn't guess in time. The number I was thinking of was {number}!")