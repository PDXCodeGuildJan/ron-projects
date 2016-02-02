"""Implement Angry Dice for one player"""

__author__ = "Ron Shafii"


from random import randint

stage_goals = {1:[1,2], 2:[3,4], 3:[5,6]}

current_stage = 1


def main():

	global current_stage

	#create 2 die
	die_1 = Die(6)
	die_2 = Die(6)
	

	display_welcome()

	while current_stage <= 3:

		roll(die_1, die_2)


		if eval_angry_die(die_1, die_2):
			current_stage = 1
			unlock_die(die_1, die_2)
			continue


		if eval_stage_complete(die_1, die_2):
			current_stage += 1
			unlock_die(die_1, die_2)
			
			if current_stage > 3:
				print ("You've Won")
				break
			else:
				print ("\nYou've reached Stage {}!\n ".format(current_stage))
				continue


		lock_die(die_1, die_2)
		eval_locked_die(die_1, die_2)






def display_welcome():


	print("Welcome to Angry Dice")
	print("Here are the rules of the game:\n")
	print("Roll two dice that require 2 consecutive integers to be returned in order to advance to the next stage.")
	print("Each die has 6 sides. The number 3 has been replaced with an Angry Face.\n")

	print("At stage 1 you must roll a one and a two to move to stage 2")
	print("At stage 2 you must roll an Angry Face (3) and a four to move to stage 3")
	print("At stage 3 you must roll a five and a six to win the game.\n")

	print("After the computer rolls the dice you will be prompted if you want to hold a die.")
	print("The computer will not automatically hold the die for you, so pay attention.\n")

	print("If you roll two Angry Faces you will be forced to restart the entire game.")
	print("You can't lock a six except on Stage 3.\n")

	input("Press ENTER to start the game!\n")





def roll(die_1, die_2):
	"""rolls the unlocked die"""

	#if die_1 isn't locked roll the die
	die_1.roll_die()

	# if die_2 isn't locked roll the die
	die_2.roll_die()


	display_die(die_1, die_2)



def display_die(die_1, die_2):
	""" displays the value of each die"""
	
	print("You rolled a {} and {}".format(die_1, die_2))



def eval_angry_die(die_1, die_2):
	"""evaluates whether user rolled 2 angry faces and returns them to stage 1"""

	if die_1.value == 3 and die_2.value == 3:
		print ("Wow you're angry! Starting Over. ")
		return True

	else:
		return False





def eval_stage_complete(die_1, die_2):
	"""evaluates whether to move to the next stage or not"""

	if die_1.value in stage_goals[current_stage] and die_2.value in stage_goals[current_stage] and die_1.value != die_2.value:
		return True

	else:
		return False
	






def lock_die(die_1, die_2):
	"""Prompts the user if they would like to lock a die. Create a die_status to pass to roll_dice() to prevent it from being rolled."""


	status_list = [die_1.locked, die_2.locked]
	if die_1.locked == False:
		die_1_status = input("Would you like to lock die_1? Press (Y)es or (N)o. ").upper()

		if die_1_status == "Y":
			die_1.locked = True

	if die_2.locked == False:
		die_2_status = input("Would you like to lock die_2? Press (Y)es or (N)o. ").upper()

		if die_2_status == "Y":
			die_2.locked = True





def unlock_die(die_1, die_2):
	"""Unlock the die after rolling"""
	die_1.locked = False
	die_2.locked = False





def eval_locked_die(die_1, die_2):
	"""Evaluate if the user is allowed to lock the die. Prompt user if unable to lock die or return to roll_dice()"""

	if die_1.locked == True:
		if die_1.value not in stage_goals[current_stage]:
			die_1.locked = False
			print("You're not allowed to lock a {} on stage {}".format(die_1.value, current_stage))

		
		elif die_1.value == 6:
			die_1.locked = False
			print("You're not allowed to lock a {} on stage {}".format(die_1.value, current_stage))

	if die_2.locked == True:
		if die_2.value not in stage_goals[current_stage]:
			die_2.locked = False
			print("You're not allowed to lock a {} on stage {}".format(die_2.value, current_stage))	

		elif die_2.value == 6:
			die_2.locked = False
			print("You're not allowed to lock a {} on stage {}".format(die_2.value, current_stage))

	if die_1.locked == True and die_2.locked == True:
		if die_1.value == die_2.value:
			print("You can only lock one die of the same value. We'll only lock die_1 for you.")
			die_2.locked = False





class Die:
	""""define the die object"""


	def __init__(self, sides):
		"""	store the number of sides"""
		self.sides = sides
		self.value = 1
		self.locked = False


	def __str__(self):
		"""displays dice value and displays angry face when required"""
		if self.value == 3:
			return "Angry Face"
		else:
			return str(self.value)		
		

	def roll_die(self):
		"""randomly genearate the value of the die """
		if self.locked == False:

			self.value = randint(1,self.sides)









if __name__ == '__main__':
	main()


