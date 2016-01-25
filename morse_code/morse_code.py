"""Implement a Morse Code translator"""


__author__ = "Ron Shafii and Shawn Waldow"

import re
#from morse import morse
import morse






def main():
	filename = "morse_to_file.txt"
	write_code(encode("This, is a test string!"), filename)
	decode(encode("This, is a test string!"))
	





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
	print(inverted_dictionary)

	# process a string of morse. Turn into a list of characters and word delimitors
	# use .split to to split message into words. separate words with 7 spaces
	words_to_decode = morse_string.split('       ')
	print(words_to_decode)


	# split the word into a list of characters (list of lists)
	# loop through the list of words and split into a list of characters
	for i in words_to_decode:
		list_of_chars = i.split('   ')
		#another_list_of_chars = re.split('   ', i)


		# loop through the listed of chars to decode with the inverted dict
		for x in list_of_chars:
			print("this is ", x)

			try:
				decoded_string += inverted_dictionary[x]
			except KeyError:
				pass

	print(decoded_string)





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






def read_code():
	"""Accepts a filename and returns the English translation of the contents of the file."""



	pass



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