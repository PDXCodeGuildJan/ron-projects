"""Implement Angry Dice for one player"""

__author__ = "Ron Shafii"





"""RULES FOR PLAYER
	Welcome message “Welcome to Angry Dice”

	Roll two dice that requires 2 consecutive integers to be returned in order to advance to 	the next stage.

	At stage 1 you must roll a one and a two to move to stage 2
	At stage 2 you must roll an Angry Face (3) and a four to move to stage 3
	At stage 3 you must roll a five and a six to win the game.

	When the computer rolls the appropriate  number for your stage you will be prompted to hold the die. 
	The computer will not automatically hold the die for you, so pay attention.

	If you roll two Angry Faces you will be forced to restart the entire game.

	"""

def main():
	#


	#create 2 die

	die_1 = Die(6)
	die_2 = Die(6)
	current_round = 1
	round_goals = {1:[1,2], 2:[3,4], 3:[5,6]}


	def roll_dice():
	"""rolls the unlocked die"""
	pass


	def dislay_dice():
	""" displays the value of each die"""
	pass


	def eval_angry_dice():
	"""evaluates wheter user rolled 2 angry faces"""
	pass


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
	"""prompts the user to lock a die if the stage isn't complete lock current_value and prevent it from being rolled again"""
	pass


	def eval_locked_die():
	"""Evaluate if the user is allowed to lock the die. Prompt user if unable to lock die or return to roll_dice()"""
	pass










class Die:
	""""define the die object"""


	def __init__(self, sides):
		"""	store the number of sides"""
		self.sides = sides
		self.value = 1


	def __str__(self):
		"""displays dice value and displays angry face when required"""
		if self.value = 3:
			return "Angry Face"
		else:
			return self.value
			
		

	def roll_die():
		"""randomly genearate the value of the die """
		self.value = randint(1,sides)









def __name__ == '__main__':
	main()

