class Test:
	h=0
	def my_fun(self,k):
		print("hii,Im in class")
		self.h=k
		print(self.h)
o=Test()
o1=Test()
o.my_fun(2)
o1.my_fun(4)
o3=Test()
print(o3.h)
