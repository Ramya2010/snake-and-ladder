def func1()
n1 = int(input("enter a number"))
n2 = int(input("enter a number"))
n3 = int(input("enter a number"))
if n1!=n2||n2!=n3||n3!=0:
	return n1+n2+n3
elif n1==n2||n2==n3||n3==n1:
	return 0
func1()