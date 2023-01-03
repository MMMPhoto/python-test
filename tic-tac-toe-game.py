# Tic Tac Toe game
import random
import sys

# Introduce player to game
print('Hello, welcome to the Tic Tac Toe game!')

# Ask player X or O
print('Would you like to be X or O?')
playerTurn = input()

# Game function
def ticTacToeGame():

    # Set gameplay dictionary
        # The keys for the following dictionary follow abbreviations that correspond to the rows of the gameplay grid:
        # First letter denotes the row, "Upper(U)", "Middle(M)", or "Lower(L)"
        # Second Letter denotes the row: "Left(L)", "Middle(M)", or "Right(R)"
        # Entire board starts with empty strings
    gameplay = {
        "UL": " ",
        "UM": " ",
        "UR": " ",
        "ML": " ",
        "MM": " ",
        "MR": " ",
        "LL": " ",
        "LM": " ",
        "LR": " "
    }

    # Explain the game
    print('The computer will go first.')

    print()
    # print(f'{name}, I am thinking of a number between 1 and 20.')

    # # Assign random number
    # secretNumber = random.randint(1, 20)

    # # Give player 6 guesses
    # for guesses in range(6):
    #     guess = 0
    #     if guesses > 0:
    #         print(f'Number of guesses remaining: {6 - guesses}')

    #     # Input validation
    #     while True:
    #         try:
    #             guess = int(input('Take a guess: '))
    #             while guess < 1 or guess > 20:
    #                 print('You must enter an integer between 1 and 20.')
    #                 guess = int(input('Take a guess: '))
    #         except ValueError:
    #             print('You must enter an integer between 1 and 20.')
    #             continue
    #         else:
    #             break
        
    #     # Check against random value
    #     if guess == secretNumber:
    #         break
    #     elif guess > secretNumber:
    #         print('Your guess is too high.')
    #     elif guess < secretNumber:
    #         print('Your guess is too low.')

    # # Either too many tries or correct guess
    # if guess == secretNumber:
    #     print(f'Good job, {name}! You guessed the number in {guesses + 1} tries')
    # else:
    #     print(f"Too bad! You couldn't guess in time. The number I was thinking of was {secretNumber}!")

    # Ask to play again
    print('Would you like to play again? (Y/N)')
    playAgain = 0
    while True:
        playAgain = input()
        if playAgain == 'Y':
            ticTacToeGame()
        elif playAgain == 'N':
            print('Okay, goodbye!')
            sys.exit()
        else:
            print('Please answer Y/N')
            continue

ticTacToeGame()