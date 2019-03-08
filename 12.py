#without parameters 
def func1():
	print("hii")
	print("hello")
func1()

#with parameters
def func2(a):
	print("hi \t",a)
func2("ramya")

#with 2/3 parameters
def func3(a,b,c):
	d=a+b+c
	print(a,b,c,d)
func3(1,2,3)

#with default parameter
def func4(university="CMR"):
	print("I am in"+"\t "+university)
func4("IIT")
func4("IIM")
func4()

#return statement
def func5(a,b,c):
	d=a+b+c
	return d
e=func5(1,2,3)
print(e)

#calling one function from other return statement
def func6(a,b):
	print("hey other function")
	c=a+b
	return c
def func7():
	print("hello,I am gonna call other function")
	s=func6(1,2)
	print("addition is",s)
func7()