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

