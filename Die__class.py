"""Create a generic Die class that allows users to pass a list of values that serve as the Die’s sides.
The model is Die class, current_value and possible_values as properties and roll() as the method"""

__author__ = "Ron Shafii"



import random

#	notes for my own use
#	list_of_random_items = random.sample(group_of_items, num_to_select)
#	first_random_item = list_of_random_items[0]




class Die:
	""""define the die object"""


	def __init__(self, sides):
		"""	stores the variable passed to sides"""
		self.possible_values = sides
		self.current_value = None
		self.roll()
		#self.current_value = random.choice(self.possible_values)




	def __str__(self):
		"""displays die's value """

		return str(self.current_value)		
		

	def roll(self):
		"""randomly genearate the value of the die """

		self.current_value = random.choice(self.possible_values)