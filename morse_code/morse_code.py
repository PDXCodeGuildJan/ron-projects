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




def write_code():
	"""Accepts an English message and filename, and writes the message in morse code to a file of the given name."""



	pass







	"""Import the test_code.txt and convert to useful python data type"""











if __name__ == '__main__':
	main()