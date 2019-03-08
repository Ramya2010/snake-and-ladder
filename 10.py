import random
l=['r','s','p']
us=0
cs=0
d={'r':'rock','p':'paper','s':'scissors'}
while True:
	#take input from user
	u=input("enter your choice, press n to discontinue")
	if u in d:
		print("user chooses",d[u])
	# exit
	if u=='n':
		print("game over")
		print("user score:",us)
		print("computer score",cs)
		if us>cs:
			print("user wins")
		elif cs>us:
			print("computer wins")
		else:
			print("it is a tie")
		exit()
	#input from computer
	c=random.choice(l)
	if c in d:
 		print("Computer chooses",d[c])
	#compare the user and computefr choice
	if u==c:
		print("tie")
	elif u=='r' and c=='p':
		cs=cs+1
		print("COMP WINS",cs)
	elif u=='s' and c=='r':
		cs=cs+1
		print("COMP WINS",cs)
	elif u=='p' and c=='s':
		cs=cs+1
		print("COMP WINS",cs)
	else:
		us=us+1
		print("user wins",us)
