def main():

	#welcome user to the program.
	print("Welcome to a basic maze. ")

	#user begins in room one with one door.
	room1()

def room1():
	#this is the room1 function
	print("You are at the beginning. You are in a room with one door.")
	startMaze = input("Do you choose to go through the door? Type yes or type any key to exit. ")
	if startMaze.lower() == "yes":
		room2()
	else:
		exit()

def room2():
	#start room 2 with while loop in case user doesn't type forward or back
	continueMaze2 = ""
	while continueMaze2 != "forward" and continueMaze2 != "back":

		#this is the room2 function
		print("You are in room 2. There is one door in front of you and one behind you.")
		continueMaze2 = input("Do you choose to go through the door in front of you? If yes then type forward, or type back to return to room 1. ")
		if continueMaze2.lower() == "forward":
			room3()
		elif continueMaze2.lower() == "back":
			room1()
		else:
			print("I'm sorry I don't understand what you typed. Choose either 'forward' or 'back'. ")

def room3():
	#start room 3 with while loop in case user doesn't type right or back
	continueMaze3 = ""
	while continueMaze3 != "right" and continueMaze3 != "back":

		#this is the room3 function
		print("You are in room 3. There is one door to your right and one behind you.")
		continueMaze3 = input("Choose right to go to the next room, or choose back to return to room 3. ")
		if continueMaze3.lower() == "right":
			room4()
		elif continueMaze3.lower() == "back":
			room2()
		else:
			print("I'm sorry I don't understand what you typed. Choose either 'right' or 'back'. ")

def room4():
	#start room 4 with while loop in case user doesn't type forward or back
	continueMaze4 = ""
	while continueMaze4 != "right" and continueMaze4 != "back":

		#this is the room4 function
		print("You are in room 4. There is one door in front of you and one behind you.")
		continueMaze4 = input("Choose right to go to the next room, or choose back to return to room 4. ")
		if continueMaze4.lower() == "right":
			room5()
		elif continueMaze4.lower() == "back":
			room3()
		else:
			print("I'm sorry I don't understand what you typed. Choose either 'right' or 'back'. ")

def room5():
	#start room 5 with while loop in case user doesn't type trapdoor or back
	continueMaze5 = ""
	while continueMaze5 != "trapdoor" and continueMaze5 != "back":

		#this is the room5 function
		print("You are in room 5. There is a trapdoor in the floor and the door behind you just came through.")
		continueMaze5 = input("Choose trapdoor to move forward or choose back to return to room 4. ")
		if continueMaze5.lower() == "trapdoor":
			room1()
		elif continueMaze5.lower() == "back":
			room4()
		else:
			print("I'm sorry I don't understand what you typed. Choose either 'trapdoor' or 'back'. ")

main()