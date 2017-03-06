def doesPlayerGoFirst():
    inputChar = ''
    while inputChar not in 'X O'.split():
        print("Who goes first?  Enter x for human, o for computer")
        inputChar = input().upper()
    if inputChar == 'X':
        return True
    else:
        return False
def getIsBeginnerMode():
    inputChar = ''
    while inputChar not in '1 0'.split():
        print("What difficulty?  Enter 0 for random movements (beginner), 1 for advanced mode")
        inputChar = input()
    if inputChar == 0:
        return True
    else:
        return False

def playAgain():
    #I thought this was a neat way to get yes or no,
    #found online
    print('Do you want to play again? (yes or no)')
    return input().lower().startswith('y')

def onePlayerMode():
    print('Do you want to play a one player game? (yes or no)')
    return input().lower().startswith('y')

def drawBoard(board):
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')

def drawFirstBoard():
    print('   |   |')
    print(' 1 | 2 | 3')
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' 4 | 5 | 6')
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' 7 | 8 | 9')
    print('   |   |')

def inputPlayerLetter():
    letter = ''
    while not (letter == 'X' or letter == 'O'):
        print('Do you want to be X or O?')
        letter = input().upper()

    if letter == 'X':
        return ['X', 'O']
    else:
        return ['O', 'X']
