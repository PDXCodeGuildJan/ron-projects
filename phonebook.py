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
	phonebook[name] = phonenumber # at the key name store a phone number
	print("New Contact: ", name, " was added with number ", phonenumber, "\n")



def deleted_contact(name):
	"""Removes a contact from the phonebook."""
	if name in phonebook:
		del phonebook[name]
		print(name, "was removed from the phonebook.\n")
	else:
		print("That contact does not exist.\n")


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


def print_phonebook():
	"""Prints every contact in the phonebook in a nice way"""
	for name in phonebook:
		print(name, " has number ", phonebook[name])







if __name__ == '__main__':
	main()


