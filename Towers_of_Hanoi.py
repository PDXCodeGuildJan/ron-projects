__author__ = "Ron Shafii"

"""Implementaiton for the Towers of Hanoi"""

# The sort_tower function will accept three parameters from which peg the tower should be moved to.
# The starting tower with all the discs is (tower1), to a desitnation peg where it should move to (tower2), 
# and the remaining spare peg (tower3) which we can temporarily use to make this happen.
# Let's start with 3 discs
def sort_tower(disc_height, tower1, tower2, tower3):
