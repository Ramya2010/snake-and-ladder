n = 10
i = 0
j = 1
count = 0
if n <= 0:
   print("Please enter a positive integer")
elif n == 1:
   print("Fibonacci sequence upto",n,":")
   print(i)
else:
   print("Fibonacci sequence upto",n,":")
   while count < n:
       print(i)
       sum = i + j
       i = j
       j = sum
       count = count + 1