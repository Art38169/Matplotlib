import matplotlib.pyplot as plt
import numpy as np

# x = np.linspace(-10, 10, 400)  # 400 points from -10 to 10

# y = x ** 2
# y1 = x * np.sin(2 * x)
# y2 = np.arctan(x)

# plt.plot(x, y, color = 'Green')
# plt.plot(x, y1, color = 'Red', linestyle = 'dashed')
# plt.plot(x, y2, color = 'Yellow', linestyle = 'dotted')
# plt.xlabel('x')
# plt.ylabel('y')
# plt.title('Graph of x^2, xsin(2x), arctg(x)')
# plt.legend()
# plt.grid(True)


# plt.show()


# fig = plt.figure(figsize = (8, 6))
# ax = fig.add_subplot(111, projection = '3d')
    
# x_vals = np.linspace(-3, 3, 50)
# y_vals = np.linspace(-3, 3, 50)
# X, Y = np.meshgrid(x_vals, y_vals)
# Z = np.sin(3 * X) * Y
    
# ax.plot_surface(X, Y, Z, cmap = 'viridis', edgecolor = 'green')
# ax.set_title('Surface Plot: z = y * sin(3x)')
# ax.set_xlabel('X')
# ax.set_ylabel('Y')
# ax.set_zlabel('Z')
# ax.grid(True)
# plt.show()

data_bars = np.loadtxt('values_for_bars.csv', delimiter=' ')
# data_hist = np.loadtxt('values_for_hist.csv', delimiter=' ')
unique_values, counts = np.unique(data_bars, return_counts=True)

plt.bar(unique_values, counts, color='orange', width=0.6)

plt.title('Bar Chart of Unique Values')
plt.xlabel('Unique Values')
plt.ylabel('Frequency')

plt.show()
print(data_bars)