# Tic Tac Toe game
import random
import sys

# Introduce player to game
print('Hello, welcome to the Tic Tac Toe game!')
comp = "O"

# Ask player X or O
print('Would you like to be X or O?')
while True:
    player = input()
    if player == "X":
        comp = "O"
        break
    elif player == "O":
        comp = "X"
        break
    else:
        print('Please answer either X or O:')
        continue

# Game function
def ticTacToeGame():

    # Set gameplay dictionary
    gameplay = {
        1: " ",
        2: " ",
        3: " ",
        4: " ",
        5: " ",
        6: " ",
        7: " ",
        8: " ",
        9: " "
    }

    # Print gameboard function
    def displayBoard(gameplay):
        print('')
        print(f"{gameplay[1]}|{gameplay[2]}|{gameplay[3]}\n-----\n{gameplay[4]}|{gameplay[5]}|{gameplay[6]}\n-----\n{gameplay[7]}|{gameplay[8]}|{gameplay[9]}")
        print('')

    # Set gameplay variables
    isComputersTurn = True
    playedSpaces = []
    global gameOver
    gameOver = False

    # Explain board input choices
    print('')
    print('To play a turn, enter a number between 1 and 9 which corresponds to an open space. \nThe top row (from left to right) is 1, 2, and 3. \nMiddle row (L to R) is 4, 5, and 6. Bottom row is 7, 8, 9.')
    print('')

    # Start game
    print('The computer will go first:')

    # Loop through game play
    for turns in range(1, 10):

        # Define move variables
        move = 0
        mark = comp

        # Player or computer moves
        if isComputersTurn:
            while move < 1 or move > 9 or move in playedSpaces:
                move = random.randint(1, 9)
                mark = comp
        else:
            # Player input validation
            while True:
                try:
                    while move < 1 or move > 9 or move in playedSpaces:
                        print('Enter a number that corresponds to an empty space to move (an integer between 1 and 9): ')
                        move = int(input())
                        mark = player
                except ValueError:
                    continue
                else:
                    break

        # Update board and played spaces tally
        gameplay[move] = mark
        playedSpaces.append(move)

        # Display of board based on gamplay dictonary
        if isComputersTurn or turns == 9:
            displayBoard(gameplay)
        
        # Check for win function
        def checkWin(a, b, c):
            global gameOver
            if gameplay[a] == gameplay[b] == gameplay[c] and gameplay[a] != " ":
                gameOver = True
                
        # Check for win
        if turns >= 5:
            checkWin(1, 2, 3)
            checkWin(4, 5, 6)
            checkWin(7, 8, 9)
            checkWin(1, 4, 7)
            checkWin(2, 5, 8)
            checkWin(3, 6, 9)
            checkWin(1, 5, 9)
            checkWin(3, 5, 7)
            if gameOver == True:
                break

        # Change turns
        isComputersTurn = not isComputersTurn

    # Determine who won game
    if len(playedSpaces) == 9:
        print("Game ended in a draw!")
    elif isComputersTurn:
        print("You lost!")
    else:
        displayBoard(gameplay)
        print("You won!")

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