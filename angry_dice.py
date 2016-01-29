"""Implement Angry Dice for one player"""

__author__ = "Ron Shafii"







def main():


	#create 2 die
	die_1 = Die(6)
	die_2 = Die(6)
	current_stage = 1
	stage_goals = {1:[1,2], 2:[3,4], 3:[5,6]}


	display_welcome()
	#if eval_angry_die = True
		#if true then return to stage 1




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
	print("You can't lock a six.\n")

	print("Press ENTER to start the game!\n")





def roll(die_1, die_2):
	"""rolls the unlocked die"""

	#if die_1 isn't locked roll the die
	if die_1.locked != True:
		die_1.roll_die()
	# if doe_2 isn't locked roll the doe
	if die_2.locked != True:
		die_2.roll_die()

	display_die(die_1, die_2)



def dislay_die(die_1, die_2):
	""" displays the value of each die"""
	
	print("You rolled a {} and {}".format(die_1, die_2))



def eval_angry_die():
	"""evaluates whether user rolled 2 angry faces and returns them to stage 1"""

	if die_1.value == 3 and die_2.value == 3:
		print ("Wow you're angry! Starting Over. ")
		return True

	else:
		return False





def eval_stage_complete():
	"""evaluates whether to move to the next stage or not"""

	pass



def update_stage():
	"""advances the user to the next stage"""




	pass



def win():
	""" tells the user when they won"""
	pass








def lock_die():
	"""Prompts the user if they would like to lock a die. Create a die_status to pass to roll_dice() to prevent it from being rolled."""

	status_list = [die_1.lock, die_2.lock]

	die_1_status = input("Would you like to lock die_1? Press (Y)es or (N)o. ").upper()

	if "Y":
		die_1.lock = True



	die_2_status = input("Would you like to lock die_2? Press (Y)es or (N)o. ").upper()

	if "Y":
		die_2.lock = True







def eval_locked_die():
	"""Evaluate if the user is allowed to lock the die. Prompt user if unable to lock die or return to roll_dice()"""

	pass










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
			return self.value
			
		

	def roll_die():
		"""randomly genearate the value of the die """
		self.value = randint(1,sides)









if __name__ == '__main__':
	main()

