# Dice Game

import random

def random_dice():
	random_dice.min = int(raw_input("Please enter min number: "))
	random_dice.max = int(raw_input("\nPlease enter max number: "))
	random_dice.roll = random.randint(random_dice.min, random_dice.max)
	
	raw_input('\nPress <ENTER> to roll...')
	
	print "\nYou roll giving you: ", random_dice.roll 
	
def pick():
	if random_dice.roll  == random_dice.max:
		print "\nyou are damm lucky man"
	else:
		print "\nCRAP!!!..You are as unlucky as your ass.... \n"
	
	
def user_confirm():

	user_confirm.confirm = ''
	
	while user_confirm.confirm not in {'Y', 'N'}:
		user_confirm.confirm = raw_input("wanna play again: (Y or N)\n").upper()
	return 	user_confirm.confirm
	
	

print "\nThis a dice game, not normal dice game. If you got the highest roll, you will get a reward.....\n"

while True:
	random_dice()
	pick()
	user_confirm()
	
	#game_on = True

	if user_confirm.confirm == 'Y':
		print "That's my boy, OH!! maybe girl\n"
		continue
	elif user_confirm.confirm == 'N':
		print "Kicking your ass... \n"
		break
	
	
	