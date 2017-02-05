# Tic Tac Toe
from UI import *
from random import randint

def getPlayerMove(board):
    move = 42 #higher than board size for first check
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not spaceIsFree(board, move):
        print('What is your next move? (1-9)')
        move = input()
    return int(move)

def getRandomMove(board):
    #random.seed()
    move = 5
    while not spaceIsFree(board, move):
        move = randint(1,9)
    return move

def copyBoard(board):
    copy = []
    for space in board:
        copy.append(space)
    return copy

def getAiMove(board, isRandom):
    if isRandom:
        return getRandomMove(board)

    if spaceIsFree(board, 5):
        return 5
    else:
        #if ai can win, play it
        for space in range(1,10):
            copy = copyBoard(board)
            if spaceIsFree(copy, space):
                copy[space] = 'O'
                if aiWon(copy):
                    return space
        #if user can win, play it
        for space in range(1,10):
            copy = copyBoard(board)
            if spaceIsFree(copy, space):
                copy[space] = 'X'
                if playerWon(copy):
                    return space
    if spaceIsFree(board, 1):
        return 1
    if spaceIsFree(board, 3):
        return 3
    if spaceIsFree(board, 7):
        return 7
    if spaceIsFree(board, 9):
        return 9
    return getRandomMove(board)


def getSpaceAsValue(i):
    if i == 'X':
        return 1
    elif i == 'O':
        return 10
    else:
        return 0

def getBoardAsValues(board):
    boardVals = [0] * 10
    boardVals[1] = getSpaceAsValue(board[1]) + getSpaceAsValue(board[2]) + getSpaceAsValue(board[3])
    boardVals[2] = getSpaceAsValue(board[4]) + getSpaceAsValue(board[5]) + getSpaceAsValue(board[6])
    boardVals[3] = getSpaceAsValue(board[7]) + getSpaceAsValue(board[8]) + getSpaceAsValue(board[9])
    boardVals[4] = getSpaceAsValue(board[1]) + getSpaceAsValue(board[4]) + getSpaceAsValue(board[7])
    boardVals[5] = getSpaceAsValue(board[2]) + getSpaceAsValue(board[5]) + getSpaceAsValue(board[8])
    boardVals[6] = getSpaceAsValue(board[3]) + getSpaceAsValue(board[6]) + getSpaceAsValue(board[9])
    boardVals[7] = getSpaceAsValue(board[1]) + getSpaceAsValue(board[5]) + getSpaceAsValue(board[9])
    boardVals[1] = getSpaceAsValue(board[3]) + getSpaceAsValue(board[5]) + getSpaceAsValue(board[7])
    return boardVals

def spaceIsFree(board, move):
    return board[int(move)] == ' '

def playerWon(board):
    boardVals = getBoardAsValues(board)
    for line in boardVals:
        if line == 3:
            return True
    return False

def aiWon(board):
    boardVals = getBoardAsValues(board)
    for line in boardVals:
        if line == 30:
            return True
    return False

def playOnePlayerGame():
    board = [' '] * 10
    board[0] = "null"
    isPlayersTurn = doesPlayerGoFirst()
    isBeginnerMode = getIsBeginnerMode()

    gameIsPlaying = True
    drawFirstBoard()

    while gameIsPlaying:
        if isTieGame(board):
            print("TIE!")
            gameIsPlaying = False
            break
        drawBoard(board)
        if isPlayersTurn:
            if aiWon(board):
                print('you lost')
                gameIsPlaying = False
                break
            move = getPlayerMove(board)
            board[move] = 'X'
            #print(type(getPlayerMove(board)))
            isPlayersTurn = False
        else:
            if playerWon(board):
                print('you won')
                gameIsPlaying = False
                break
            move = getAiMove(board, isBeginnerMode)
            board[move] = 'O'
            isPlayersTurn = True
def isTieGame(board):
    for index, space in enumerate(board):
        if space == ' ':
            print(index)
            return False
    if not playerWon(board) and not aiWon(board):
        return True

def playTwoPlayerGame():
    board = [' '] * 10
    board[0] = "null"
    print("Player 1 is X, Player 2 is O")

    gameIsPlaying = True
    drawFirstBoard()

    while gameIsPlaying:
        drawBoard(board)
        if isTieGame(board):
            print("TIE!")
            gameIsPlaying = False
            break
        if isPlayersTurn:
            if aiWon(board):
                print('Player 2 won')
                gameIsPlaying = False
            move = getPlayerMove(board)
            board[move] = 'X'
            isPlayersTurn = False
        else:
            if playerWon(board): #re-using this method because player2 is O
                print('Player 1 won')
                gameIsPlaying = False
            move = getPlayerMove(board)
            #print(getPlayerMove(board))
            board[move] = 'O'
            isPlayersTurn = True

while True:
    if onePlayerMode():
        playOnePlayerGame()
    else:
        playTwoPlayerGame()

    if not playAgain():
        break
