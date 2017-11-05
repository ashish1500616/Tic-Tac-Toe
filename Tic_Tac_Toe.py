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

# function to ask player the choice index and fill the index if empty
def ask_player(mark):
    ''' Asks player where to place X or O mark, checks validity '''
    global board
    req = 'Choose where to place your: ' + mark
    while True:
        try:
            choice = int(input(req))
        except ValueError:
            print("Sorry, please input a number between 1-9.")
            continue

        if choice not in range(1,10):
            print("Sorry, please input a number between 1-9.")
            continue

        if board[choice] == " ":
            board[choice] = mark
            break
        else:
            print ("That space isn't empty!")
            continue

#function to take the players Choice.

def player_choice(mark):
    global board,game_state,announce
    #Set game blank game announcement
    announce = ''
    #Get Player Input
    mark = str(mark)
    # Validate input
    ask_player(mark)

    #Check for player win
    if win_check(board,mark):
        clear_output()
        display_board()
        announce = mark +" wins! Congratulations"
        game_state = False
    
    #Show board
    clear_output()
    display_board()

    #Check for a tie 
    if full_board_check(board):
        announce = "Tie!"
        game_state = False
        
    return game_state,announce

#binding up all the function in a play_game function.
def play_game():
    reset_board()
    global announce
    
    # Set marks
    X='X'
    O='O'
    while True:
        # Show board
        clear_output()
        display_board()
        
        # Player X turn
        game_state,announce = player_choice(X)
        print(announce)
        if game_state == False:
            break
            
        # Player O turn
        game_state,announce = player_choice(O)
        print (announce)
        if game_state == False:
            break
    
    # Ask player for a rematch
    rematch = raw_input('Would you like to play again? y/n')
    if rematch == 'y':
        play_game()
    else:
        print ("Thanks for playing!")
    