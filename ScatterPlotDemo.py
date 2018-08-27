import matplotlib.pyplot as plt
x = [2, 3, 4, 5, 7, 9]
y = [3, 6, 8, 4, 1, 4]
plt.scatter(x,y, label="stars", color="blue", marker="*", s=60)
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title("Scatter Plot")
plt.legend()
plt.show()
