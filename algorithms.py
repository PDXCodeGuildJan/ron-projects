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



#####################################################


def insertion_sort(myList):

	####################
	#STEP 1
	####################
	# Begin at the start of the unsorted list
	# make sorted list begin at the start of the unsorted list
	# define how sort length changes for each iteration
	starting_index = 1
	sort_length = starting_index

		
	while startingIndex  < len(myList):



		####################
		#STEP 2
		####################
		while current_index != 0 and myList[current_index] < myList[current_index - 1]:



			####################
			#STEP 3
			####################
			# compare current number with next adjacent number
			# is number in current position greater than adjacent position?
			if myList[current_index] > myList[current_index + 1]:
			



				####################
				#STEP 4
				####################
				# swap the numbers 
				myList = swap(myList, current_index, current_index + 1)
			
 

			###################
			#STEP 5
			###################
			#repeat until list is sorted, and shift end of list by one
			current_index += 1
			

		sort_length += 1


	return myList



def main():
	myList = [58, 8, 99, 1, 56]
	print(myList)
	myList = insertion_sort(myList)
	print(myList)


#swap function
def swap(myList, index1, index2):
	temp_item = myList[index1]
	myList[index1] = myList[index2]
	myList[index2] = temp_item

	return myList



main()
