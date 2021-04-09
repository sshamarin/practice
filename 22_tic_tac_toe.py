import pprint
the_board = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
        'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
        'low-L': ' ', 'low-M': ' ', 'low-R': ' '}

def printBoard(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-+-+-')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-+-+-')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])

turn = 'X'
for i in range(9):
    printBoard(the_board)
    move = input('turn for %s. pick any position: ' % turn)
    the_board[move] = turn # refreshing our dictionary (content for game board))
    if turn == 'X': # change player in the end of the turn
        turn = 'O'
    else:
        turn = 'X'

printBoard(the_board)
