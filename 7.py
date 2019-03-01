import random
d = {8:37,33:7,67:2,55:5,3:4}
p=random.choice([8,33,67,55,3])
print("you got",p)
if p in d:
	if p>d[p]:
		print("swallowed by a snake")
	else:
		print("climb the ladder")
	print("you can go to",d[p])
