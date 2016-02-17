"""Implement an MVC Mastermind game for one player. This file is the controller."""

__author__ = "Ron Shafii"


import mastermind_model
import mastermind_view
import random



class MasterMind:


	def __init__(self):
		pass



	def generate_goal(self):
		"""create 4 randomly generated colored pegs to establish the goal of the game."""
		goal = []
		for x in range(4):
			player_peg = mastermind_model.PlayerPeg(random.choice(mastermind_model.MasterModel.peg_colors))
			goal.append(player_peg)
		return goal 




	def play_game():
		"""plays the mastermind game"""

		#Show the game rules and objectives


		#prompt the user to enter 4 colors


		#check if the user won


			#if the user didn't win evaluate the player's peg colors against the computer_peg colors
			#if no colors match display to the user Nothing to display


				#if player colors match then evaluate if any of the player's pegs position match the computer's peg positions
				#return the appropriate position and color matches to the player

			#decrement the number of guesses left
			#display to the user the number of guesses left before they lose the game
			#if the number of guesses == 0 then display they lost the game.

			#loop back to prompt the user to enter 4 colors 


		pass


	def check_win():
		"""checks to see if the player's guess (mastermind_model.Guess.player_peg) exactly matches the 
		4 computer generated pegs (mastermind_model.MasterModel.goal). """
		
		#takes the results stored from prompt_user and turns it into a True or False statement

		# check if player_peg1 == computer_peg1

		#check if player_peg2 == computer_peg2

		#check if player_peg3 == computer_peg3

		#check if player_peg4 == computer_peg4



		#if [mastermind_model.Guess.player_peg] == goal
		#	print ("You Win!")
		# if not Win then forward the info to eval_peg_color()






	def eval_peg_color():
		"""Evaluates whether the player's peg colors matches any of the computer's colors. 
		Results are stored by class Guess in the model. """

		#check if player_peg1 color matches any computer_peg color

		#check if player_peg2 color matches any computer_peg color

		#check if player_peg3 color matches any computer_peg color

		#check if player_peg4 color matches any computer_peg color
		pass

	def eval_peg_position():
		"""Evaluates whether any of the matched colors from eval_peg_color also match the 
		correct peg positions and returns a black or white peg as necessary. """

		#check if player_peg1 position is the same as computer_peg1 position

		#check if player_peg2 position is the same as computer_peg2 position

		#check if player_peg3 position is the same as computer_peg3 position

		#check if player_peg4 position is the same as computer_peg4 position



			keypeg1 = mastermind_model.KeyPeg(KeyPeg.SMALL_BLACK)
		pass





def test():
	#testing the random color generator
	test_object = MasterMind()
	temp_list = test_object.generate_goal()
	for peg in temp_list:
		print(peg.color)


test()

