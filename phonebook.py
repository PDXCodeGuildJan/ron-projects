"""Implement a simple phonebook using a dictionary."""

__author__ = "Ron Shafii"

import re



# add global phonebook to prevent having to call functions.
# initialize the dictionary that will store out phone numbers.
phonebook = {}

def main():
	"""The main driver function of our phonebook."""

	#load any existing data into phonebook
	load_phonebook()
	#print("Phonebook after load:", phonebook)

	print("Welcome to the phonebook.")

	option = ""

	while option != "E":

		# Ask the user what they want to do
		option = input("You can: \n\t(A)dd\n\t(D)elete\n\t(P)rint\n\t(S)earch by name\n\tsearch by (N)umber\n\t(E)xit \n\tWhich would you like to choose? ")

		if option.upper() == "A":
			name = input("What is the contact's name? ")
			number = input("What is the " + name + "'s number? ")
			add_contact(name, number)

		elif option.upper() == "D":
			name = input("What contact name are you removing? ")
			delete_contact(name)

		elif option.upper() == "E":
			print("Goodbye")
			exit()

		elif option.upper() == "P":
			print_phonebook()

		elif option.upper() == "S":
			name = input("What contact name do you want to locate? ")
			search(name)

		elif option.upper() == "N":
			search_number = input("What number did you want to search? ")
			search_by_number(search_number)

		else:
			print("I'm sorry I didn't understand. ")



def add_contact(name, phonenumber):
	"""Does an addition to the phonebook with the given contact info."""

	# remove extra white space that can be added in input
	regex = "\s+\Z"
	thing_you_replace_with = ""
	scrubbed_name = re.sub(regex, thing_you_replace_with, name)
	print(scrubbed_name)


	# scrub and reformat the phone number to follow (xxx) xxx-xxxx pattern
	# remove all, but the numbers
	regex = "[0-9]+"
	nums = re.findall(regex, phonenumber)
	new_num = ""
	for every_num in nums:
		new_num += every_num

	# introduce the correct formatting
	formatted_num = "(" + new_num[0:3] + ") " + new_num[3:6] + "-" + new_num[6:]
	#print(formatted_num)


	phonebook[scrubbed_name] = formatted_num # at the key name store a phone number
	print("New Contact: ", scrubbed_name, " was added with number ", formatted_num, "\n")

	#save updated phonebook
	save_phonebook()



def delete_contact(name):
	"""Removes a contact from the phonebook."""
	if name in phonebook:
		del phonebook[name]
		print(name, "was removed from the phonebook.\n")
	else:
		print("That contact does not exist.\n")

		#save updated phonebook
		save_phonebook()


def search(name):
	"""Find who a certian number is associated with."""
	if name in phonebook:
		number = phonebook[name]
		print(name, "'s number is", number, "\n")

	else:
		print("Sorry no contact exists with that name.\n")



def search_by_number(search_number):
	"""Determine who is associated with a certain number"""
	for name, number in phonebook.items():
		if search_number == number:
			print(number, "is associated with the name ", name, "\n")
			result = name
			break

	if result == "":
		print("Sorry, there is no contact with that number.")



def save_phonebook():
	"""Save contents of the phonebook to a file"""
	open_file = open("PDXphonebook.txt", "w")
	open_file.write(str(phonebook)) #cast dictionary into a string
	open_file.close()



def load_phonebook():
	"""load phonebook data from the saved file"""
	global phonebook #allows load to update global phonebook

	#if the file doesn't exist then create it in append mode and close it
	load_file = open("PDXphonebook.txt", "a")
	load_file.close()


	#if the file exists then open it in read mode
	load_file = open("PDXphonebook.txt", "r")
	phonebook_data = load_file.read() #variable to catch data into
	load_file.close()


	if phonebook_data:
		# if phonebook has data, load it into the dictionary
		# convert from string back to dictionary
		# can't  cast a string dicrectly to a dictionary using dict().  use eval() instead.
		# phonebook = dict(phonebook_data)
		phonebook = eval(phonebook_data)
		# print(phonebook)



def print_phonebook():
	"""Prints every contact in the phonebook in a nice way"""
	for name in phonebook:
		print(name, " has number ", phonebook[name])







if __name__ == '__main__':
	main()


