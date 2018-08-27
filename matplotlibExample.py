import matplotlib.pyplot as plt
x1 = [1,3,1]
y1 = [2,4,1]
plt.plot(x1,y1,color='blue',linestyle='dashed',linewidth=3,marker='o',markerfacecolor='green',markersize=12)

plt.ylim(1,10)
plt.xlim(1,10)

plt.xlabel('x-axis')
plt.ylabel('y-axis')

plt.title('My First Graph')

plt.show()
