
__author__ = "Ron Shafii"


from creature_class import Creature
from monster import Monster

class Hero(Creature):
	"""Create and define the Hero class that will inherit properties from the Creature class"""




	def __init__(self):
	# in this case super will be Creature
		#super.__init__(self)
		super(Hero, self).__init__()

		self.level = 1







class Monster_hero(Monster, Hero):
	"""create a new class that inherits from Monster and Hero"""



	def __init__(self):

		Monster.__init__(self)
		Hero.__init__(self)



		self.second_weapon = None
