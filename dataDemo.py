import matplotlib.pyplot as plt
import csv

x = []
y = []

with open('data.csv','r') as csvfile:
    plots = csv.reader(csvfile)
    for col in plots:
        x.append((col[0]))
        y.append((col[1]))

plt.plot(x, y, label='File')
plt.xlabel('X')
plt.ylabel('Y')
plt.title("Dataset")

plt.legend()
plt.show()
