#Tic Tac Toe game

#prints the game field
def game_field(position_dic):

	print('\n'*100)

	for i in range(1,10):
		if i % 3 != 0:
			print(f'| {position_dic[i]} ', end = "")
		else:
			print(f'| {position_dic[i]} ', end = "|\n")
			print('--------------')

#takes an integer between 1 and 9 that's going to be used as position

def checker(position_dic, position):
	return position_dic[position] == ' '

def user_input(position_dic):
	
	position = 0

	while position not in range(1,10) or not checker(position_dic, position):
		position = int(input('Please input position number from 1 to 9: '))

	return int(position)


def player_choice():

	player = input('Please choose the first player (X/O): ')
	if player == 'X':
		return True
	elif player =='O':
		return False
	else:
		print('Please insert either an X or an O.')
		player_choice()

def victory_check(position_dic):

	victory = False

	if position_dic[1] == position_dic[2] == position_dic[3] != ' ':
		victory = True
	elif position_dic[4] == position_dic[5] == position_dic[6] != ' ':
		victory = True
	elif position_dic[7] == position_dic[8] == position_dic[9] != ' ':
		victory = True
	elif position_dic[1] == position_dic[4] == position_dic[7] != ' ':
		victory = True
	elif position_dic[2] == position_dic[5] == position_dic[8] != ' ':
		victory = True
	elif position_dic[3] == position_dic[6] == position_dic[9] != ' ':
		victory = True
	elif position_dic[1] == position_dic[5] == position_dic[9] != ' ':
		victory = True
	elif position_dic[3] == position_dic[5] == position_dic[7] != ' ':
		victory = True
	elif ' ' not in position_dic.values():
		victory = 'Draw'
	else:
		victory = False
	
	return victory


#game logic inside
#Needs victory condition, seriously, how to generalize? || There's a condition now, but it's very brutal and inefficient
def game_loop():

	position_dic = {1:' ',2:' ',3:' ',4:' ',5:' ',6:' ',7:' ',8:' ',9:' '}
	
#turn_x is to be remade into a choice of who's starting.
	
	playing = True

	if player_choice() == True:
		turn_x = True
	else:
		turn_x = False


	while playing:

		if victory_check(position_dic) == 'Draw':
			print("It's a draw!")
			break
		elif victory_check(position_dic) == True:
			print(f"{player} has won!")
			break

		if turn_x == True:
			player = 'X'

		else:
			player = 'O'

		position = user_input(position_dic)
		
		position_dic[position] = position_dic[position].replace(' ', player)

		game_field(position_dic)
		turn_x = not turn_x

game_loop()