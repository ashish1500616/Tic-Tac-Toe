import os
clear =lambda :os.system('cls')

#Global Variables

board =[' '] * 10
game_state=True
announce =''

# Reset Function
def reset_board():
	global board,game_state
	board=[' ']*10
	game_state=True

# function to display the board
def display_board():
	clear()
    print "  "+board[7]+" |"+board[8]+" | "+board[9]+" "
    print "------------"
    print "  "+board[4]+" |"+board[5]+" | "+board[6]+" "
    print "------------"
    print "  "+board[1]+" |"+board[2]+" | "+board[3]+" "

#function to check win_status
def win_check(board, player):
    ''' Check Horizontals,Verticals, and Diagonals for a win '''
    if (board[7]  ==  board[8] ==  board[9] == player) or \
        (board[4] ==  board[5] ==  board[6] == player) or \
        (board[1] ==  board[2] ==  board[3] == player) or \
        (board[7] ==  board[4] ==  board[1] == player) or \
        (board[8] ==  board[5] ==  board[2] == player) or \
        (board[9] ==  board[6] ==  board[3] == player) or \
        (board[1] ==  board[5] ==  board[9] == player) or \
        (board[3] ==  board[5] ==  board[7] == player):
        return True
    else:
        return False

#function to check the full board whether the board is full empty.
def full_board_check(board):
    if " " in board[1:]:
        return False
    else:
        return True