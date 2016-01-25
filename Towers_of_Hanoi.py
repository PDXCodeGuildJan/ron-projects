__author__ = "Ron Shafii"

"""Implementaiton for the Tower of Hanoi"""

# The sort_tower function will accept three parameters from which peg the tower should be moved to.
# The starting tower with all the discs is (start), to a destination peg where it should move to (end), 
# and the remaining spare peg (temp) which we can temporarily use to make this happen.

# Let's start with 3 discs
def move_to_tower(disc_height, start, temp, end):
	#if disc height is 1 then move from source to destination
	if disc_height >= 1:

	    else:
	    	#move all discs except the very last one from start to the temp using the end 
	        move_to_tower(disc_height-1, start, temp, end)


	        # move last disc to the end
	        move_to_tower(start, end)

	        # nive all discs from temp to end using the start as needed
	        move_to_tower(disc_height-1, temp, end, start)


	


# create a move_disc function to swap discs from tower to tower?
def move_a_disc(start, end)