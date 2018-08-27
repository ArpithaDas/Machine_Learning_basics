import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0, 2*(np.pi), 0.1)
y1 = np.cos(x)
y2 = np.sin(x)

plt.plot(x, y1, label='cos')
plt.plot(x, y2, label='sin')


'''x1 = [0, 1, 2, 3, 4, 5, 6, 7]
y1 = [0, 1, 0, -1, 0, 1, 0, -1]
plt.plot(x1,y1)

x2 = [0, 1, 2, 3, 4, 5, 6, 7]
y2 = [1, 0, -1, 1, 0, -1, 1, 0]
plt.plot(x2,y2)

plt.xlabel('x-axis')
plt.ylabel('y-axis')

plt.xlim(0,10)
plt.ylim(-5,5)'''

plt.legend()
plt.show()
