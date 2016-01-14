def selection_sort(myList):
	#####################
	#STEP 1
	####################
	# Begin at the start of the unsorted list
	startingIndex = 0
		
	while startingIndex  < len(myList):


		####################
		#STEP 2
		####################
		# look at every item in unsorted list (loop through list)

		# then locate smallest number in unsorted list
		indexSmallest = startingIndex

		for currentIndex, value in enumerate(myList[startingIndex:]):
			if myList[indexSmallest] > value:
				indexSmallest = currentIndex


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
		print(myList)



	###################
	#STEP 5
	#####################
	#repeat until unsorted list is empty
	return myList




def main():
	myList = [5, 8, 1, 0, 3]
	print(myList)
	myList = selection_sort(myList)
	print(myList)

main()
