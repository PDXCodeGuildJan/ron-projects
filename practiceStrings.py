def main():
	myString = "shortString"
	print(myString[1])
	print(myString[-3])
	print(myString[4:7])

	userinput = input("Please type a word. ")

	#add string for middle index algorithm
	middle_characters("elephant")
	
	#accept input from user and pass to sequence
	stringSequence(userinput)

#determine middle index of a string
def middle_characters(the_string):
	middle = (len(the_string) // 2)
	print(the_string[middle-1:middle+2])

#write a function that expects an input of a sequence and prints the sequence
def	stringSequence(string):
	print(string)
	for x in string:
		print(x)
	

main()