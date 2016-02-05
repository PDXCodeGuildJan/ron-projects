"""Create and define the Monster class that inherits properties from the Creature class"""

__author__ = "Ron Shafii"


from creature_class import Creature

class Monster(Creature):

	AGGRO = "aggressive"
	DEFENSE = "defensive"



	def __init__(self):
	# in this case super will be Creature
		#super.__init__(self)
		super(Monster, self).__init__()

		self.personality = Monster.AGGRO

