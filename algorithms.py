def selection_sort(myList):
	#####################
	#STEP 1
	####################
	# Begin at the start of the unsorted list
	startingIndex = 0
		
	while startingIndex  < len(myList):

		print("Starting big loop with startingIndex:", startingIndex)
		####################
		#STEP 2
		####################
		# look at every item in unsorted list (loop through list)

		# then locate smallest number in unsorted list
		indexSmallest = startingIndex

		for currentIndex in range(startingIndex, len(myList)):
			print("Looking at currentIndex:", currentIndex, "with value:", myList[currentIndex])
			if myList[indexSmallest] > myList[currentIndex]:
				indexSmallest = currentIndex
				print("new lowest value:", myList[currentIndex])


		####################
		#STEP 3
		####################
		#swap smallest number with first number in unsorted list by creating a temp item
		myList = swap(myList, startingIndex, indexSmallest)


		#temp_item = myList[startingIndex]
		#myList[startingIndex] = myList[indexSmallest]
		#myList[indexSmallest] = temp_item


		####################
		#STEP 4
		####################
		#increase starting index by 1 of unsorted list
		startingIndex += 1
		print("Current state of the whole list:", myList)



	###################
	#STEP 5
	#####################
	#repeat until unsorted list is empty
	return myList




#####################################################




def bubble_sort(myList):

	####################
	#STEP 1
	####################
	# Begin at the start of the unsorted list
	# define how sort length changes for each iteration
	starting_index = 0
	sort_length = len(myList)

		
	while sort_length > starting_index:


		####################
		#STEP 2
		####################
		current_index = starting_index

		while current_index < sort_length -1:



			####################
			#STEP 3
			####################
			# compare current number with next adjacent number
			# is number in current position greater than adjacent position?
			if myList[current_index] > myList[current_index + 1]:



				####################
				#STEP 4
				####################
				# swap the numbers when current number is greater than adjacent number
				myList = swap(myList, current_index, current_index + 1)


				#temp_item = myList[current_index]
				#myList[current_index] = myList[current_index + 1]
				#myList[current_index + 1] = temp_item
			


			###################
			#STEP 5
			###################
			#repeat until list is sorted, and shift end of list by one
			current_index += 1
			print(current_index, sort_length)

		sort_length -= 1


	return myList





#########################################################


def insertion_sort(myList):
	pass
	####################
	#STEP 1
	####################
	# Start of outer loop
	# Begin at the start of the unsorted list
	# make sorted list begin one index value to the right of the start of the unsorted list
	for index in range(1, len(myList)):

		
		#get the current index value. we'll call it current_value
		current_value = myList[index]

		#get the adjacent value to the left of the current_value. This is a temp index.
		adjacent = index



		####################
		#STEP 2
		####################
		# start of inner loop
		# compare current_value with adjacent_value
		# is current_value greater than adjacent_value?
		while (adjacent < (myList[adjacent - 1] and adjacent > 0)):
		#while adjacent > 0 and index < myList[adjacent - 1]:
		#while adjacent >= 0:
			#if current_value < myList[adjacent]


			#swap the value with adjacent value
			swap(myList, adjacent, adjacent - 1)




			###################
			#STEP 3
			###################
			#repeat until list is sorted
			adjacent -= 1


	return myList





########################################################

def merge_sort(myList):

	"""Implement merge_sort algorithm"""


	####################
	#STEP 1
	####################
	# define the segments in the unsorted list
	# Split the unsorted list into two segments
	if len(myList) <= 1:
		return myList

	else:
		mid = len(myList) // 2
		


		####################
		# STEP 3
		####################
		#sort the first half
		left_segment = merge_sort(myList[:mid])


		#sort the 2nd half
		right_segment = merge_sort(myList[mid:])




		####################
		#STEP 4
		####################
		# merge the two segments back into one sorted list
		return merge(left_segment, right_segment)







##################################################


def merge(left_segment, right_segment):
	"""Implement merge function"""


	# we need two dynamic indexes
	left_index = 0
	right_index = 0
	returned_list = []

	# merge the left sorted segment with the right sorted segment to create a 3rd list
	while left_index < len(left_segment) and right_index < len(right_segment):
		#top of left segment is smaller
		if left_segment[left_index] < right_segment[right_index]:
			returned_list.append(left_segment[left_index])
			left_index += 1

			#top of right segment is smaller
		else:
			returned_list.append(right_segment[right_index])
			right_index += 1

	#copy remaining items from left segment and append
	while left_index < len(left_segment):
		returned_list.append(left_segment[left_index])
		left_index += 1

	#copy remaining items from right segment and append
	while right_index < len(right_segment):
		returned_list.append(right_segment[right_index])
		right_index += 1

	return returned_list



####################################################









def main():
	myList = ["e", "z", "l", "o", "f", "b"]
	print(myList)
	myList = merge_sort(myList)
	print(myList)


####################################################

#swap function
def swap(myList, index1, index2):

	"""Implement swamp function"""


	temp_item = myList[index1]
	myList[index1] = myList[index2]
	myList[index2] = temp_item

	return myList


# call the main to sort the values
if __name__ == "__main__":
	main()
