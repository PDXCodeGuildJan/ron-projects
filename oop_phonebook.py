"""Phonebook implemented with classes."""

__author__ = "Ron Shafii"

import re



class Contact:
	"""Defines the contact object to store info about people"""
	#require user to submit first name and last name
	def __init__(self, f_name, l_name):
		#assign pased arguments to their corresponding properties
		self.first_name = f_name
		self.last_name = l_name
		self.phone_num = ""
		self.addresses = {}
		self.email = ""


	def update_address(self, addy_key, street="", unit="", city="", state="", zip_code="", country=""):
		"""Update the address at addy_key (home, work) with the info passed."""

		pass



	def format_phone_num(self, phone_num):
		"""Format the phone number of the contact"""

		pass

	def print_contact(self):
	"""Print out the contact info"""
		pass




class Address:
	"""Defines the Address object to be used with Contact"""

	def __init__(self):
		self.street = ""
		self.unit = ""
		self.city = ""
		self. state = ""
		self.zip_code = ""
		self.country = ""


	def __str__(self):
		"""Print out the formatted address"""
		formatted_str = sel.street

		if self.unit != "":
			formatted_str = "\n" + self.unit
		
		formatted_str = "\n" + self.city + " " + self.state
		formatted_str = "\n" + self.zip_code
		formatted_str = "\n" + self.country

		return formatted_str








if __name__ == '__main__':
	main()


