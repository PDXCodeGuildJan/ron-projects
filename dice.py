from random import randint

# Create a die function that returns a random number, as if 
# the user rolled a die.
def die():
   roll = randint(1, 6)
   print(roll)


# Make a function called custom_die that takes a range 
# and print a random number in that range.
def custom_die(num1, num2):
	roll = randint(num1, num2)

	#determine if max or min
	if roll == num1:
		print(num1, "Critical Fail")
	elif roll == num2:
		print(num2, "Critical Hit")
	else:
		print(roll)

def main():
	print("Welcome to die roller, press q to exit")

	entree = ""

	#wrap the core logic of the function in a while loop
	#so that it keeps asking to roll until we exit
	while entree != "q":


		# Ask the user how many dice to roll
		entree = input("How many Dice rolls do you want to roll? ")
		if entree == "q":
			# Exit the program
			exit()
		total_rolls = int(entree)

		#Find out how big the Dice are
		entree = input("How many sides on the Dice? ")
		if entree == "q":
			# Exit the program
			exit()
		total_sides = int(entree)

		# Roll that many dice
		for something in range(0, total_rolls):
			custom_die(1, total_sides)


main()