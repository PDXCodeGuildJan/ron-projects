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
		pass


	def check_win():
		"""checks to see if the player's guess (mastermind_model.Guess.player_peg) exactly matches the 
		4 computer generated pegs (mastermind_model.MasterModel.goal). """
		
		#takes the results stored from prompt_user and turns it into a True or False statement



		#if [mastermind_model.Guess.player_peg] == goal
		#	print ("You Win!")



	def eval_peg_color():
		"""Evaluates whether the player's peg colors matches any of the computer's colors. 
		Results are stored by class Guess in the model. """
		pass

	def eval_peg_position():
		"""Evaluates whether any of the matched colors from eval_peg_color also match the 
		correct peg positions and returns a black or white peg as necessary. """
		pass





def test():
	#testing the random color generator
	test_object = MasterMind()
	temp_list = test_object.generate_goal()
	for peg in temp_list:
		print(peg.color)


test()

