import random
points = dict({'king':100,'minister':80,'inspector':50,'theif':0})   #assign all the values that the roles take in a dictionary

game_points = {}   								#dictionary to store the game points of the players later
role = {}									#empty dictionary to map the roles to the players

def calc(keys):
	if role[keys] not in game_points:							
		game_points[role[keys]] = points[keys]
	else:
		game_points[role[keys]] = game_points[role[keys]] + points[keys]

			


def game():					#main game starts from here
	players = []			#empty list to store the player names through the console
	for n in range(4):
		name = raw_input("Insert the players name : ")
		players.append(name)		#Take 4 players input and keep appending to the list

	print "The list of players are ", players ,"\n"

	sample = random.sample(players,4)			#randomly select the four players and assign the role to items
	
	role['king'] = sample[0]
	role['minister'] = sample[1]
	role['inspector'] = sample[2]
	role['theif'] = sample[3]

	
	
	print "King:",role['king'],"           -->         Minister:",role['minister']
	print "\n"
	print "Who stole my Queens necklace???"
	print "\n"
	guess = raw_input("Minister a name                    ---->                  ")  #guess the theif
	print "\n"
	if guess in role['theif']:											#if the guess is correct
		print "Kill the thief",role['theif']
		for keys in points.keys():
			if keys == 'king':											#if the role is king/minister/inspector/theif add the points to the players dictionary "game_points"
				calc(keys)
			if keys == 'minister':
				calc(keys)			
			if keys == 'inspector':
				calc(keys)			
			if keys == 'theif':
				calc(keys)
				
	else:
		print "Kill the minister",role['minister'] 			# if the guess is wrong
		for keys in points.keys():
			if keys == 'king':
				calc(keys)
				
			if keys == 'inspector':
				calc(keys)
				
			if keys == 'minister':										#if guess is wrong add ministers points to thief and vice versa
				if role[keys] not in game_points:
					game_points[role[keys]] = points['theif']
				else:
					game_points[role[keys]] = game_points[role[keys]] + points['theif']
			
			if keys == 'theif':
				if role[keys] not in game_points:
					game_points[role[keys]] = points['minister']
				else:
					game_points[role[keys]] = game_points[role[keys]] + points['minister']

def choice():
	answer = raw_input("Do yu want to continue(y/n) ? ")
	return answer

while True:
	game()
	print "\n",role
	if choice() == 'n':
		print "\n",game_points
		break

	
	
	
	