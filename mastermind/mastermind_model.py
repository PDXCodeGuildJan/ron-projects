"""Implement an MVC Mastermind game for one player.
This file is the model."""

__author__ = "Ron Shafii"


class MasterModel:
	"""determines #of guesses, computer generated goal, and history of player's guesses"""



	def __init__(self):
		self.guess_num = None #keeps track of the player guess counter
		self.goal = [] #four random computer generated pegs
		self.guesses = [] #appended list of all player's guesses for the whole game
		self.key_list = [] #list of previous computer responses to the player




class Guess:
	"""stores guess of player pegs and key pegs"""

	def __init__(self, peg1, peg2, peg3, peg4):
		#build out the pieces that exist in the model
		#self.peg1 = [] #list strings that stores player's current guess (4 colored pegs each guess)
		#self.key_peg = [] #list that stores the key pegs (black and white pegs that match player's guesses)
		self.peg1 = peg1
		self.peg2 = peg2
		self.peg3 = peg3
		self.peg4 = peg4



class PlayerPeg:
	"""define the 6 colored pegs used by the player and randomly generated by the computer to choose 4 pegs"""

	RED ="red"
	GREEN = "green" 
	BLUE = "blue"
	YELLOW = "yellow"
	BLACK = "black"
	WHITE = "white" 

	def __init__(self, color):
		"""store the color of the peg"""
		self.color = color


	def __str__(self):

		return str(self.color)


class KeyPeg:
	"""define the key peg"""

	#globals inside the key_peg class
	SMALL_BLACK = "small_black"
	SMALL_WHITE = "small_white"


	def __init__(self, color):
		"""store the color of the peg"""
		self.color = color

	def __str__(self):

		return str(self.color)