import random 
#Ask the user to enter the game mode 
def selectGameMode():
    print('Select game mode:')
    print("1: 3x6 board")
    print("2: 4x9 board") 

    gameMode = input()
    while int(gameMode) != 1 and int(gameMode) != 2: 
        print("Please, select one opction: 1 or 2")    
        gameMode = input() 
    return int(gameMode)  

#Get initial score base onf the gameMode selected 
def getInitialScore(gameMode): 
    if gameMode == 1:
        return 150 
    else: 
        return 300 
    
#Get initial board base on the gameMode selected    
def getInitialBoard(gameMode): 
    if gameMode == 1:
        board = [
            [' ', ' ', ' ', ' ', ' ', ' '], 
            [' ', ' ', ' ', ' ', ' ', ' '], 
            [' ', ' ', ' ', ' ', ' ', ' ']
        ]
        return board
    if gameMode ==2:  
        board = [
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], 
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], 
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
        ]
        return board

#Print the game board
def printGameBoard(board): 
    for row in board: 
        print(row) 

def userPlay(gameMode): 
    userRow = int(input("Enter the row number: "))
    if gameMode == 1: 
        while userRow < 1 or userRow > 3: 
            print("Please, select a valid row number: 1,2,3") 
            userRow = int(input("Enter the row number: "))
    else: 
        while userRow < 1 or userRow > 4: 
            print("Please, select a valid row number: 1,2,3,4") 
            userRow = int(input("Enter the row number: "))
    userRow = userRow - 1
    return userRow 

def randomPlay(gameMode): 
    if gameMode == 1: 
        randomRow = random.randint(0,2) 
    else: 
        randomRow = random.randint(0,3)
    return randomRow 

def updateBoard(userRow,randomRow,board,currentColumn): 
    if userRow == randomRow: 
        board[randomRow][currentColumn] = 'X'
    else: 
        board[randomRow][currentColumn] = "2" 
        board[userRow][currentColumn] = "1"
    return board 

def checkState(gameMode,userRow,randomRow,currentColumn):
    if userRow == randomRow: 
        return "Game Over"
    else: 
        currentColumn = currentColumn + 1 
        if gameMode == 1: 
            if currentColumn >= 6: 
                return "Win"
            else:
                return "Continue"
        else: 
            if currentColumn >= 9: 
                return "Win"  
            else:
                return "Continue"   

def updateScore(score,state): 
    if state == "Game Over": 
        score = score - 50 
        return score
    if state == "Continue": 
        score = score + 20 
        return score
    return score

def game(gameMode,score,board,currentColumn): 

    userRow = userPlay(gameMode) 
    randomRow = randomPlay(gameMode) 
    board = updateBoard(userRow,randomRow,board,currentColumn) 
    printGameBoard(board)
    state = checkState(gameMode,userRow,randomRow,currentColumn)
    score = updateScore(score,state) 
    return score, state

def playAgain(): 
    print("Do you want to play again? (yes/no)")
    playAgain = input()
    while playAgain != "yes" and playAgain != "no":
        print("Please, enter a valid option: yes or no")
        playAgain = input()
    return playAgain


gameMode = selectGameMode() 
print("Game mode selected: ", gameMode)
score = getInitialScore(gameMode) 
board = getInitialBoard(gameMode) 
printGameBoard(board) 
currentColumn = 0 
score,state = game(gameMode,score,board,currentColumn)
playAgain = "yes" 

while score > 0 and playAgain == "yes"and state != "Win": 
    if state == "Game Over":
        print("Game Over!") 
        print("Your final score is: ", score)
        playAgainUser = playAgain()
        
        if playAgain == "yes": 
            board = getInitialBoard(gameMode) 
            printGameBoard(board) 
            currentColumn = 0 
            score,state = game(gameMode,score,board,0)
        else:
            print("Thanks for playing!") 
            print("Your final score is: ", score)
    else:
        print("Your current score is: ", score)
        currentColumn = currentColumn + 1
        score,state = game(gameMode,score,board,currentColumn)

if score < 0: 
    print("You lost!")
    print("Your final score is: ", score)

if state == "Win": 
    print("Congratulations! You win!")
    print("Your final score is: ", score)
    print("Thanks for playing!")