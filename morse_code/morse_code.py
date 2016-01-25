"""Implement a Morse Code translator"""


__author__ = "Ron Shafii and Shawn Waldow"

import re
#from morse import morse
import morse






def main():
	filename = "test_code.txt"
	#write_code(encode("This, is a test string!"), filename)
	#decode(encode("This, is a test string!"))
	print(read_code(filename))






def decode(morse_string):
	"""decodes morse into english"""
	#split dict into a list of tuples
	#inverse_temp_list = morse.morse.items()
	#initialize dictionary
	inverted_dictionary = {}
	decoded_string = []

	#build an inverted dict line by line
	for (k,v) in morse.morse.items():
		# turn key into value and value into the key
		# change list of tuples back into a dictionary
		inverted_dictionary[v] = k


	# process a string of morse. Turn into a list of characters and word delimitors
	# use .split to to split message into words. separate words with 7 spaces
	words_to_decode = morse_string.split('          ')



	# split the word into a list of characters (list of lists)
	# loop through the list of words and split into a list of characters
	for i in words_to_decode:
		list_of_chars = i.split('   ')
		#another_list_of_chars = re.split('   ', i)
		# setup tracking variables
		length = len(list_of_chars)
		counter = 0

		# loop through the listed of chars to decode with the inverted dict
		for x in list_of_chars:


			# ignore invalid morse strings
			try:
				decoded_string += inverted_dictionary[x]


				# check to see if we've reached the end. if so then insert a space
				# maintain the counter to make sure it keeps up with the FOR loop
				counter += 1

				# if counter reaches end of list_of_chars insert a space
				if counter == length:
					decoded_string += ' '


			except KeyError:
				pass


	# turn list of translated characters back into a list of strings
	# decoded_string_to_pass is a list not a string
	decoded_string_to_pass = ''.join(decoded_string)

	return decoded_string_to_pass







def encode(words_to_encode):

	"""encodes english into morse"""
	#there are 3 spaces between letters, and 7 spaces between words
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
			#NEED TO CHANGE ALIAS morse.morse for legibility
			letter = morse.morse[letter.upper()]

			temp_word += letter
			# add 3 spaces to the end of each character
			temp_word += "   "

			# are we at the end of the word
			if index == length - 1:
				temp_word += "    "


			index += 1
		# appending results of each character into a list
		list2.append(temp_word)
		# converting the appended words in the list into a string
		list2_string = ''.join(map(str, list2))

	return(list2_string)






def read_code(filename):
	"""Accepts a filename and returns the English translation of the contents of the file."""
	open_file = open(filename, "r")
	# name the contents of the file morse_string
	morse_string = open_file.read()
	open_file.close()
	# call the function decode to translate the morse string into an english string
	return decode(morse_string)




# write code takes two arg the first is an english string and the other is a string that's a filename
def write_code(english_string, filename):

	"""Accepts an English message and filename, and writes the message in morse code to a file of the given name."""

	# if the file doesn't exist then create it in append mode and close it
	open_file = open(filename, "w")
	open_file.write(english_string)
	open_file.close()



	"""Import the test_code.txt and convert to useful python data type"""











if __name__ == '__main__':
	main()