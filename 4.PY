import random

while True:
	r=input("Press r to roll, q to quit :")

	if r=='r':
		print("you get :",random.randint(1,6))
		elif r=='q':
			print("BYE")
			exit()