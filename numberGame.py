# Guess the number game
import random
import sys

# Ask player for name
print('Hello, what is your name?')
name = input()

# Game function
def numberGame():
    # Explain the game
    print(f'{name}, I am thinking of a number between 1 and 20.')

    # Assign random number
    number = random.randint(1, 20)

    # Give player 6 guesses
    for num in range(6):
        guess = 0
        if num > 0:
            print(f'Number of guesses remaining: {6 - num}')

        # Input validation
        while True:
            try:
                guess = int(input('Take a guess: '))
                while guess < 1 or guess > 20:
                    print('You must enter an integer between 1 and 20.')
                    guess = int(input('Take a guess: '))
            except ValueError:
                print('You must enter an integer between 1 and 20.')
                continue
            else:
                break
        
        # Check against random value
        if guess == number:
            break
        elif guess > number:
            print('Your guess is too high.')
            continue
        elif guess < number:
            print('Your guess is too low.')
            continue

    # Either too many tries or correct guess
    if guess == number:
        print(f'Good job, {name}! You guessed the number in {num + 1} tries')
    else:
        print(f"Too bad! You couldn't guess in time. The number I was thinking of was {number}!")

    # Ask to play again
    print('Would you like to play again? (Y/N)')
    playAgain = 0
    while True:
        playAgain = input()
        if playAgain == 'Y':
            numberGame()
        elif playAgain == 'N':
            print('Okay, goodbye!')
            sys.exit()
        else:
            print('Please answer Y/N')
            continue

numberGame()