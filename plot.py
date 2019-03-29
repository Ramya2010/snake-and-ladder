import matplotlib.pyplot as plt 
x=[1,2,3,4,5]
y=[5,7,3,9,10]
# naming the x axis 
plt.xlabel('x - axis') 
plt.ylabel('y - axis') 
  # giving a title to my graph 
plt.title('My first graph!') 
plt.bar(left, height, tick_label = tick_label, 
        width = 0.8, color = ['red', 'green']) 
plt.plot(x,y)
plt.show()