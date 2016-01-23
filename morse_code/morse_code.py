"""Implement a Morse Code translator"""


__author__ = "Ron Shafii and Shawn Waldow"

import re
import morse




def main():
	print(encode("This, is a test string!"))
	





def decode():
	"""decodes morse into english"""

	pass




def encode(words_to_encode):
	"""encodes english into morse"""
	#there are 3 breaks between letters, and 7 breaks between words
	#split a string into a list of words
	list1 = words_to_encode.split()
	list2 = []

	#loop through list for every word
	for word in list1:

		#loops through every letter in word
		length = len(word)
		index = 0
		temp_word = ""

		#look through each letter in the word
		while index < length:
			letter = word[index]
			#lookup each letter in morse.py
			letter = morse.morse[letter.upper()]

			temp_word += letter

			index += 1

		list2.append(temp_word)


	return(list2)






def read_code():
	"""Accepts a filename and returns the English translation of the contents of the file."""



	pass



# write code takes two arg the first is an english string and the other is a string that's a filename
def write_code(english_string, filename):

	"""Accepts an English message and filename, and writes the message in morse code to a file of the given name."""
	temp_list = encode(english_string)
	#locate list funciton that passes a list as a string
	# add breaks to create spaces between letters and words



	#if the file doesn't exist then create it in append mode and close it
	load_file = open(filename, "a")
	load_file.close()

	#need to

	open_file = open(filename, "w")
	open_file.write(astring)
	open_file.close()



	"""Import the test_code.txt and convert to useful python data type"""











if __name__ == '__main__':
	main()