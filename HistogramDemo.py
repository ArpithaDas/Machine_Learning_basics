import matplotlib.pyplot as plt
ages = [2, 5, 67,34, 12, 37, 78,12,34,22,34, 56, 45, 87, 65, 90, 12, 43 ,2,7]
range = (0, 100)
bins = 10
plt.hist(ages, bins, range, color='blue', histtype = 'bar', rwidth=0.8)
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('Histogram')
plt.show()
