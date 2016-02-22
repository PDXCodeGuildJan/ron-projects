"""Create and define the Creature class that will later be used to create a Monster"""

__author__ = "Ron Shafii"



class Weapon:
	"""weapon object creatures can use"""

	def __init__(self, attack_value):
		self.base_damage = attack_value



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
		"""return the attack value of the creature given its base attack value, weapon attack value and state"""


		attack_value = self.attack_points

		#if we have a weapon add the weapond's damaage to attack_value
		if self.weapon:
			attack_value += self.weapon.base_damage


		#return total calculated damage
		#return self.attack_points
		return attack_value




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