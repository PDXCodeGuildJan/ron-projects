"""Implement a simple phonebook using a dictionary."""

__author__ = "Ron Shafii"



# add global phonebook to prevent having to call functions.
# initialize the dictionary that will store out phone numbers.
phonebook = {}

def main():
	"""The main driver function of our phonebook."""

	print("Welcome to the phonebook. ")

	option = ""

	while option != "E":

		# Ask the user what they want to do
		option = input("You can: \n\t(A)dd\n\t(D)elete\n\t(P)rint\n\t(S)earch by name\n\t(E)xit \n\tWhich would you like to choose? ")

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
			number = input("What contact name do you want to locate? ")

		else:
			print("I'm sorry I didn't understand. ")



def add_contact(name, phonenumber):
	"""Does an addition to the phonebook with the given contact info."""
	phonebook[name] = phonenumber # at the key name store a phone number
	print("New Contact: ", name, " was added with number ", phonenumber, "\n")



def deleted_contact(name):
	"""Removes a contact from the phonebook."""
	del phonebook[name]



def search(name):
	"""Find who a certian number is associated with."""
	number = phonebook[name]
	print(name, "'s number is", number, "\n")



def print_phonebook():
	"""Prints every contact in the phonebook in a nice way"""
	for name in phonebook:
		print(name, " has number ", phonebook[name])







if __name__ == '__main__':
	main()


