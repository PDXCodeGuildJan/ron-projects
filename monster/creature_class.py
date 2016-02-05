"""Create and define the Creature class that will later be used to create a Monster"""

__author__ = "Ron Shafii"







class Creature:

	#globals inside the class
	NORMAL = "normal"
	ASLEEP = "asleep"
	UNCONS = "unconscious"
	POISONED = "poisoned"
	WEAKENED = "weakened"


	

	def __init__(self):
		"""Store the creature properties"""
		self.name = ""
		self.state = Creature.NORMAL
		self.health = 20
		self.max_health = 20
		self.attack_points = 2
		self.weapon = None
		self.special_abilities = {}
		self.stats = {}
		





	def attack(self):
		pass




	def heal(self):
		pass




	def defend(self):
		pass




	def take_damage(self):
		pass




	def change_weapon(self, new_weapon):
		pass




	def change_state(self, new_state):
		pass





	def __str__(self):
		"""displays creature's stats """

		return str(self.stats)		






if __name__ == '__main__':
	main()