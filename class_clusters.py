import matplotlib.pyplot as plt
import numpy as np

points = np.loadtxt('points.csv', delimiter=',')
x = points[:, 0]
y = points[:, 1]

plt.scatter(x, y)

plt.xlabel('X values')
plt.ylabel('Y values')
plt.title('Scatter Plot of 2D Data')

plt.show()
