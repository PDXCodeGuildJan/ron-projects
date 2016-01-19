#Search functions, including binary.

from algorithms import selection_sort





def main():
	unsorted_list = ["e", "z", "l", "o", "f", "b"]
	target_value = "b"

	#call the search funciton, catch what it returns
	sorted_list, target_index = binary_search(unsorted_list, target_value)


	#print out solutions
	print("I found ", target_value, "It's at ", target_index)

def binary_search(the_list, target_value):
	#implements the binary search algorithm

	#first sort the list
	sorted_list = selection_sort(the_list)

	# search for the target value
	

	# find length of current segment
	length = len(sorted_list)

	# initialize start and end variables
	start = 0
	end = length 

	# if length >= 1, look for target
	while length >= 1:
		# find the midpoint of the segment we're looking in
		
		mid = start + (length // 2)


		# determine if the middle value is greater or less than or equal
		# if equal we've found it, return to middle value (efficieny first)
		if sorted_list[mid] == target_value:
			return (sorted_list, mid)

		# if greater than, reduce the segment to first half (left half), repeat loop
		elif sorted_list[mid] > target_value:
			end = mid

		# if less than, reduce the segment to the last half (right half), repeat loop
		elif sorted_list[mid] < target_value:
			start = mid + 1

		# reevaluate length before loop runs again
		length = len(sorted_list[start:end])
		

	# if we can't find the index return negative one
	return(sorted_list, -1)




	

#call main to sort things
if __name__ == "__main__":
	main()