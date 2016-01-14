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
		temp_item = myList[startingIndex]
		myList[startingIndex] = myList[indexSmallest]
		myList[indexSmallest] = temp_item


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




def main():
	myList = [5, 8, 99, 0, 5]
	print(myList)
	myList = selection_sort(myList)


main()
