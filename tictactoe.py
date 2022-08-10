from random import shuffle

board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
wins = [ [0,1,2], [3,4,5], [6,7,8], [0,3,6], [1,4,7], [2,5,8], [0,4,8], [2,4,6]]

def printBoard():
    # print (board[0],'', board[1],'', board[2])
    # print (board[3],'', board[4],'', board[5])
    # print (board[6],'', board[7],'', board[8])

    print ()
    print ('| ', end='')
    for square in range(0,9):
        print (board[square], '| ', end='') 
        if square == 2 or square == 5:
            print ()
            print ('- - - - - - -')
            print ('| ',end='')
    print ()
    print()

def checkWin(player):
    win = False
    for test in wins:
        # print (test)
        count = 0
        for squares in test:
            if board[squares] == player:
                count += 1
            if count == 3:
                win = True
        if win:
            return win
    return win

def wipeBoard():
    global board
    for square in range(0, len(board)):
        board[square] = ' '

def canMove(): # see if move can be made
    move = False
    for square in range(0, len(board)):
        if board[square] == ' ':
            move = True
    return move

def play():
    printBoard()
    print ('Tic-Tac-Toe')
    print ('two players')
    while True:
        player_turn = 'X'
        while checkWin(swapPlayer(player_turn)) == False and canMove() == True:
            getMove(player_turn)
            printBoard()
            player_turn = swapPlayer(player_turn)
        if checkWin(swapPlayer(player_turn)):
            print('Player', swapPlayer(player_turn), 'wins ... New Game')
        else:
            print('A draw. ... New Game')
        wipeBoard()
        printBoard()
        

def playAI():
    global board
    print ('Tic-Tac-Toe')
    print ('Play against the computer AI level 0')
    printBoard()
    while True:
        player_turn = 'X'
        while checkWin(swapPlayer(player_turn)) == False and canMove() == True:
            if player_turn == 'X':
                getMove(player_turn)
            else:
                generateMove()
            printBoard()
            player_turn = swapPlayer(player_turn)
        if checkWin(swapPlayer(player_turn)):
            print ('Player', swapPlayer(player_turn), 'wins ... New Game')
        else:
            print ('A draw ... New Game')
        wipeBoard()
        printBoard()

def generateMove():
    global board
    moves = list()
    for squares in range(0, len(board)):
        if board[squares] == ' ':
            moves.append(squares)
    shuffle(moves)
    board[moves[0]] = 'O'
    print ('My move is ', moves[0]+1)


def swapPlayer(player):
    if player == 'X':
        player = 'O'
    else:
        player = 'X'
    return player

def getMove(player):
    global board
    correct_number = False
    while correct_number == False:
        square = input('Square to place the ' + player + ' : ')
        try:
            square = int(square)
        except:
            square = -2
        square -= 1 # make input number match internal numbers
        if square >= 0 and square < 10: # number in range
            if board[square] == ' ': # if it is blank
                board[square] = player
                correct_number = True
            else:
                print ('Square already occupied')
        else:
            print ('Incorrect square try again')

if __name__ == '__main__':
    playAI()
