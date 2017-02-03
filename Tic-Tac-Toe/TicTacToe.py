# Tic Tac Toe
import UI

def getPlayerMove(board):
    move = 42 #higher than board size for first check
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not spaceIsFree(board, move):
        print('What is your next move? (1-9)')
        move = input()
    return int(move)

def getAiMove(board):
    values = getBoardAsValues(board)

#def getBoardAsValues(board):


def spaceIsFree(board, move):
    return board[int(move)] == ' '


def takeUserMove(playerChar):


def playOnePlayerGame():
    board = [' '] * 10
    isPlayersTurn = doesPlayerGoFirst()
    isBeginnerMode = isBeginnerMode()

    gameIsPlaying = True
    drawFirstBoard()

    while gameIsPlaying:
        drawBoard(board)
        if isPlayersTurn:
            if playerWon(board):
                print('you won')
                gameIsPlaying = False
            move = getPlayerMove(board)
            board[move] = 'X'
            isPlayersTurn = False
        else:
            if aiWon(board):
                print('you lost')
                gameIsPlaying = False
            move = getAiMove(board)
            board[move] = 'O'
            isPlayersTurn = True

def playTwoPlayerGame(){
    board = [' '] * 10

    print("Player 1 is X, Player 2 is O")

    gameIsPlaying = True
    drawFirstBoard()

    while gameIsPlaying:
        drawBoard(board)
        if isPlayersTurn:
            if playerWon(board):
                print('Player 1 won')
                gameIsPlaying = False
            move = getPlayerMove(board)
            board[move] = 'X'
            isPlayersTurn = False
        else:
            if aiWon(board): #re-using this method because player2 is O
                print('Player 2 won')
                gameIsPlaying = False
            move = getPlayerMove(board)
            board[move] = 'O'
            isPlayersTurn = True
}

while True:
    if onePlayerMode():
        playOnePlayerGame()
    else:
        playTwoPlayerGame()

    if not playAgain():
        break
