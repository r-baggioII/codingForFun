import random

# Ask the user to enter the game mode
def selectGameMode():
    print('Select game mode:')
    print("1: 3x6 board")
    print("2: 4x9 board")

    gameMode = input()
    while gameMode not in ['1', '2']:
        print("Please, select one option: 1 or 2")
        gameMode = input()
    return int(gameMode)

# Get initial score based on the game mode selected
def getInitialScore(gameMode):
    if gameMode == 1:
        return 150
    else:
        return 300

# Get initial board based on the game mode selected
def getInitialBoard(gameMode):
    if gameMode == 1:
        board = [
            [' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ']
        ]
    elif gameMode == 2:
        board = [
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
        ]
    return board

# Print the game board
def printGameBoard(board):
    for row in board:
        print(row)

# Get the row number from the user based on the game mode
def userPlay(gameMode):
    userRow = int(input("Enter the row number: "))
    max_row = 3 if gameMode == 1 else 4
    while userRow < 1 or userRow > max_row:
        print(f"Please, select a valid row number: 1-{max_row}")
        userRow = int(input("Enter the row number: "))
    return userRow - 1

# Get a random row number based on the game mode
def randomPlay(gameMode):
    return random.randint(0, 2) if gameMode == 1 else random.randint(0, 3)

# Update the board after each play
def updateBoard(userRow, randomRow, board, currentColumn):
    if userRow == randomRow:
        board[randomRow][currentColumn] = 'X'
    else:
        board[randomRow][currentColumn] = "2"
        board[userRow][currentColumn] = "1"
    return board

# Check the current state of the game
def checkState(gameMode, userRow, randomRow, currentColumn):
    if userRow == randomRow:
        return "Game Over"
    currentColumn += 1
    max_columns = 6 if gameMode == 1 else 9
    return "Win" if currentColumn >= max_columns else "Continue"

# Update the score based on the game state
def updateScore(score, state):
    if state == "Game Over":
        score -= 50
    elif state == "Continue":
        score += 20
    return score

# Main game loop
def game(gameMode, score, board, currentColumn):
    userRow = userPlay(gameMode)
    randomRow = randomPlay(gameMode)
    board = updateBoard(userRow, randomRow, board, currentColumn)
    printGameBoard(board)
    state = checkState(gameMode, userRow, randomRow, currentColumn)
    score = updateScore(score, state)
    return score, state

# Check if the user wants to play again
def playAgain():
    print("Do you want to play again? (yes/no)")
    playAgainResponse = input().lower()
    while playAgainResponse not in ["yes", "no"]:
        print("Please, enter a valid option: yes or no")
        playAgainResponse = input().lower()
    return playAgainResponse

# Game setup
gameMode = selectGameMode()
print("Game mode selected:", gameMode)
score = getInitialScore(gameMode)
board = getInitialBoard(gameMode)
printGameBoard(board)
currentColumn = 0
score, state = game(gameMode, score, board, currentColumn)
playAgainResponse = "yes"

# Game loop
while score > 0 and playAgainResponse == "yes" and state != "Win":
    if state == "Game Over":
        print("Game Over!")
        print("Your final score is:", score)
        playAgainResponse = playAgain()

        if playAgainResponse == "yes":
            board = getInitialBoard(gameMode)
            printGameBoard(board)
            currentColumn = 0
            score, state = game(gameMode, score, board, currentColumn)
        else:
            print("Thanks for playing!")
            print("Your final score is:", score)
    else:
        print("Your current score is:", score)
        currentColumn += 1
        score, state = game(gameMode, score, board, currentColumn)

if score <= 0:
    print("You lost!")
    print("Your final score is:", score)

if state == "Win":
    print("Congratulations! You win!")
    print("Your final score is:", score)
    print("Thanks for playing!")
