"""Phonebook implemented with classes."""

__author__ = "Ron Shafii"

import re



def main():

	# test the Contact and Address classes with Jim Everyperson
	jim = Contact("Jim", "Everyperson")
	jim.phone_num = "1234567890"
	jim.email = "jim@gmail.com"
	jim.update_address("Home", city="Portland")
	jim.update_address("Work", "4500 Main Street", "Bldg G", "Vancouver", "B.C.", "78D9GW", "Canada")
	print(jim)



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


	def update_address(self, addy_key, street=None, unit=None, city=None, state=None, zip_code=None, country=None):
		"""Update the address at addy_key (home, work) with the info passed."""

		

		if addy_key in self.addresses:
			temp_adddress = self.addresses[addy_key]
		else:
			# Make a new address object
			temp_address = Address()
		#set the new address' street to whatever was passed
		if street:
			temp_address.street = street
		if street:
			temp_address.unit = unit
		if street:
			temp_address.city = city
		if street:
			temp_address.state = state
		if street:
			temp_address.zip_code = zip_code
		if street:
			temp_address.country = country

		# assign the address to the given address key for the Contact
		self.addresses[addy_key] = temp_address






	def format_phone_num(self, phone_num):
		"""Format the phone number of the contact"""

		# scrub and reformat the phone number to follow (xxx) xxx-xxxx pattern
		# remove all, but the numbers
		regex = "[0-9]+"
		nums = re.findall(regex, phone_num)

		# take evertyhing int he list of numbers and make it into a string of nums
		new_num = ""
		for every_num in nums:
			new_num += every_num

		# introduce the correct formatting
		formatted_num = "(" + new_num[0:3] + ") " + new_num[3:6] + "-" + new_num[6:]
		
		#Save formatted number to Contact
		self.phone_num = formatted_num




	def __str__(self):
		"""Print out the contact info"""

		# initialize formatted string
		formatted_str = "\n{0} {1}".format(self.first_name, self.last_name)
		if self.phone_num:
			# format the phone number
			self.format_phone_num(self.phone_num)
			#add the formatted phone number to the formatted string
			formatted_str += "\nPhone: {0}".format(self.phone_num)

		#if there is an email address
		if self.email:
			formatted_str += "\nEmail: {0}".format(self.email)

		#If there is at least one address
		if self.addresses:
			formatted_str += "\n\nAddresses:"
			#add separator for console screen
			formatted_str += "\n-------------------------------------"

			#Loop through all the addresses and print them
			#get all the key, value pairs of the addresses using the dictionary.items function
			for key, address in self.addresses.items():
				#addy_key:
				formatted_str += "\n{0}:".format(key)
				#street
				formatted_str += "\n{0}".format(str(address))
				#add separator for console screen
				formatted_str += "\n------------"


		return formatted_str


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
		#tells any object in this class how to print itself when it's called
		"""Print out the formatted address instead of separate print statements"""
		formatted_str = self.street

		if self.unit != "":
			formatted_str += "\n" + self.unit
		#formatted_str = "{0}, {1}", format(self.street, self.unit)
		formatted_str += "\n" + self.city + " " + self.state
		formatted_str += "\n" + self.zip_code
		formatted_str += "\n" + self.country

		return formatted_str








if __name__ == '__main__':
	main()


