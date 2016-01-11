def main():
	myString = "shortString"
	print(myString[1])
	print(myString[-3])
	print(myString[4:7])
	middle_characters("elephant")

def middle_characters(the_string):
	middle = (len(the_string) // 2)
	print(the_string[middle-1:middle+2])

main()