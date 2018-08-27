import matplotlib.pyplot as plt
left = [1,2,3,4,5]
height = [10, 24, 36, 40, 5]
names = ['one', 'two', 'three', 'four', 'five']
plt.bar(left,height,tick_label = names, width = 0.8, color= ['blue','green'])
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.show()
