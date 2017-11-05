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

	