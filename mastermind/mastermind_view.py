"""Implement an MVC Mastermind game for one player.
This file is the view."""

__author__ = "Ron Shafii"


class MasterView:


	def show_rules(self):
		"""Displays the rules of Mastermind to the player. """
		print("Welcome to Mastermind!")

		print("Object of the Game\n")
		print("The computer picks a sequence of 4 pegs, each one being one of any of six colors:\n")
		print("red, green, blue, yellow, black, and white.")
		print("The object of the game is to guess the exact positions of the colors in the -\n")
		print("sequence in as few guesses as possible. After each guess, the computer -\n")
		print("gives you a score of exact and partial matches. A black peg indicates an exact -\n")
		print("match, a white peg a partial match (right color, wrong position)\n\n")

		print("Rules")
		print("1. The sequence can contain pegs of colors: red, green, blue, yellow, black, and white.\n")
		print("2. A color can be used any number of times in the sequence.\n")
		print("3. Each guess must consist of 4 peg colors - no blank space are allowed.\n")
		print("4. You are must guess the computer's sequence within 10 guesses, otherwise you lose the game.\n\n")



	def show_player_peg(self):
		"""displays the list of pegs chosen by the player during the current Guess."""

		pass


	def prompt_user(self):
		"""Prompts the user to choose 4 colored pegs."""
		pass


	def win(self):
		"""Displays to the player "They Won!" """
		pass



	def lose(self):
		"""Displays to the player "Sorry, You Lose." """
		pass


	def show_key_peg(self):
		"""Displays a series of black or white key pegs stored in the class Guess."""
		pass



