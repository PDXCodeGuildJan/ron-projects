"""Implement an MVC Mastermind game for one player.
This file is the controller."""

__author__ = "Ron Shafii"


import mastermind_model
import mastermind_view








class MasterMind:


	def __init__(self):
		self.model: MasterModel
		self.view: MasterView
		self.goal: MasterModel



	def generate.goal():
		"""create 4 randomly generated colored pegs to establish the goal of the game."""
		goal = []
		for x in range(4)
			player_peg = mastermind_model.Player_Peg(random.choice(mastermind_model.MasterModel.peg_colors))
			goal.append(player_peg)
			return mastermind_model.MasterModel.goal #= goal




	def play_game():
		"""plays the mastermind game"""
		pass


	def check_win():
		"""checks to see if the player's guess exactly matches the 4 computer generated pegs """
		pass


	def eval_peg_color():
		"""Evaluates whether the player's peg colors matches any of the computer's colors. 
		Results are stored by class Guess in the model."""
		pass

	def eval_peg_position():
		"""Evaluates whether any of the matched colors from eval_peg_color also match the 
		correct peg positions and returns a black or white peg as necessary. """
		pass



