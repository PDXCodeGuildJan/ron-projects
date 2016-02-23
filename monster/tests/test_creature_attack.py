__author__ = "Ron Shafii"

import unittest
from creature_class import Creature, Weapon

#import the class where the function lives that you're testing from creature import creature

#Make a TestCase, CreatureAttackTest that inherits from unittest.TestCase
class CreatureAttackTest(unittest.TestCase):


	#make the things and do the setup that every test in the TestCase needs.
	def setUp(self):
		"""Create an instance of the Creature class that we can leverage its fuctions in our tests."""

		self.creature = Creature()


	#undo everything that setUp created
	def tearDown(self):
		"""Delete the Creature instance we made in the setUp."""

		del self.creature




	def test_attack_return_int(self):
		""""Ensure when an attack is called an integer is returned"""

		#call the attack function of creature and store what it returns in value
		value = self.creature.attack()

		#self.assertIs(value, 3, "Returned attack value in not an int.")
		self.assertIsInstance(value, int, "Returned attack value in not an int.")


	def test_no_weapon_return_base_damage(self):
		"""Ensure that with no weapon the creature does its base damage"""


		#manually set the base damage to 3
		self.creature.attack_points = 2

		#get the creature's attack value
		value = self.creature.attack()

		self.assertEqual(value, 2, "Expected base attack value not given.")

	def test_with_Weapon_return_base_damage(self):
		"""Ensure that a creature with a weapon does base damage + Weapon damaage."""


		#make a weapon to give to the creature
		weapon = Weapon(3)


		#give the weapon to the creature
		self.creature.weapon = weapon

		#Set the creature's base attack value
		self.creature.attack_points = 1

		#get the creature's total attack value
		value = self.creature.attack()

		#assert the attack value is the base + weapon damage
		self.assertEqual(value, 4, "Expected base attack value and weapon value not given")

