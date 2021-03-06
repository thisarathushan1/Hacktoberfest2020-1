#TICTACTOEGAME-PROJECT
def startgame(symbol_list):
	while symbol_list[0]!='X' or symbol_list[0]!='O':
		symbol_list[0]= input("Player 1: Choose X or O: ")
		if symbol_list[0] == 'X':
			symbol_list[1] = 'O'
			break
		elif symbol_list[0]=='O':
			symbol_list[1] = 'X'
			break

def player_input(board_pos,count,symbol_list):
	x = int(input('Choose a number from 1-9: '))
	count[0]+=1
	if(count[0]%2!=0):
		board_pos[x]=symbol_list[0]
	else:
		board_pos[x]= symbol_list[1]

def display_board(board_pos):
	print("\t {} | {} | {}\n\t----------\n\t {} | {} | {}\n\t----------\n\t {} | {} | {}".format(board_pos[1],board_pos[2],board_pos[3],board_pos[4],board_pos[5],board_pos[6],board_pos[7],board_pos[8],board_pos[9]))

def gamelogic(board_pos):
	result = False
	for x in [3,6,9]:
		if board_pos[x]==board_pos[x-2] and board_pos[x]==board_pos[x-1] and board_pos[x]!='':
			result = True
	for x in [1,2,3]:
		if board_pos[x]==board_pos[x+3] and board_pos[x]==board_pos[x+6] and board_pos[x]!='':
			result = True
	if board_pos[1]==board_pos[5] and board_pos[1]==board_pos[9] and board_pos[1]!='':
		result = True
	if board_pos[3]==board_pos[5] and board_pos[3]==board_pos[7] and board_pos[3]!='':
		result = True
	return result		

def game():
	count = [0]
	symbol = ['','']
	board_pos = ['#','','','','','','','','','']
	result = False
	print('WELCOME TO TICTACTOE!')
	reply = input('Are you ready to play: YES or NO?: ')
	while reply=='YES':
		startgame(symbol)
		while ('' in board_pos):
			player_input(board_pos,count,symbol)
			print('\n')
			display_board(board_pos)
			result = gamelogic(board_pos)
			if result==True:
				if(count[0]%2!=0):
					print('\n\nPlayer 1 wins!!')
				else:
					print('\n\nPlayer 2 wins!!')
				break
		reply = input('Do you want to play again: YES or NO: ') 
		board_pos = ['#','','','','','','','','','']
	if reply == 'NO':
		print('Thank You for Your Time!!')

game()				

