from random import randint

def die():
	roll = randint(1, 6)
	print(roll)

def custom_die(num1, num2):
	roll = randint(num1, num2)
	print(roll)

die()
custom_die(10, 100)
custom_die(145, 200)
