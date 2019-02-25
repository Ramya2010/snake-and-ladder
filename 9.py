import random
l=['r','s','p']
while True:
	#take input from user
	u=input("enter your choice, press n to discontinue")
	#to exit
	if u=='n':
		print("game over")
		exit()
	#input from computer
	c=random.choice(l)
	print("Computer chooses",c)
	#compare the user and computefr choice
	if u==c:
		print("tie")
	elif u=='r' and c=='p':
		print("COMP WINS")
	elif u=='r' and c=='s':
		print("user wins")
	elif u=='s' and c=='r':
		print("computer wins")
	elif u=='s' and c=='p':
		print("user wins")
	elif u=='p' and c=='r':
		print("user wins")
	elif u=='p' and c=='s':
		print("computer wins")
	

