"""This file contains functions that test angry_dice modules. This file cannot be run on its own."""



def test_eval_locked_die():
	"""test to see if eval_locked_die() evaluates whether we can lock a die or not"""

	#modify testing current_stage to update
	global current_stage
	current_stage = 2
	#create 2 die
	die_1 = Die(6)
	die_2 = Die(6)
	#give the die values
	die_1.value = 2
	die_2.value = 2
	#lock both die
	die_1.locked = True
	die_2.locked = True

	eval_locked_die(die_1, die_2)

	print(die_1.locked, die_2.locked)




def test_unlock_die():
	"""test to see if unlock_die unlocks a locked die"""

	global current_stage
	current_stage = 1
	#create 2 die
	die_1 = Die(6)
	die_2 = Die(6)
	#give the die values
	die_1.value = 2
	die_2.value = 2
	#lock both die
	die_1.locked = True
	die_2.locked = True

	unlock_die(die_1, die_2)

	print(die_1.locked, die_2.locked)





def test_eval_angry_die():
	"""Test to see if eval_angry_die() works"""

	global current_stage
	current_stage = 1
	#create 2 die
	die_1 = Die(6)
	die_2 = Die(6)
	#give the die values
	die_1.value = 3
	die_2.value = 3
	#lock both die
	die_1.locked = False
	die_2.locked = False

	eval_angry_die(die_1, die_2)

	print(die_1.value, die_2.value)






def test_lock_die():
"""Shawn is incorrect"""
	global current_stage
	current_stage = 2

	#create 2 die
	die_1 = Die(6)
	die_2 = Die(6)

	#give the die values
	die_1.value = 2
	die_2.value = 2

	#lock both die
	die_1.locked = False
	die_2.locked = False



	lock_die(die_1, die_2)

	print(die_1.locked, die_2.locked)







def test_eval_stage_complete():


	global current_stage

	current_stage = 1

	#create 2 die
	die_1 = Die(6)
	die_2 = Die(6)

	#give the die values
	die_1.value = 3
	die_2.value = 2


	lock_die(die_1, die_2)

	print(eval_stage_complete(die_1, die_2))





if __name__ == '__main__':

	test_eval_locked_die()

	test_unlock_die()

	test_eval_angry_die()

	test_lock_die()

	test_eval_stage_complete()
