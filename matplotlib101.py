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


fig = plt.figure(figsize = (8, 6))
ax = fig.add_subplot(111, projection = '3d')
    
x_vals = np.linspace(-3, 3, 50)
y_vals = np.linspace(-3, 3, 50)
X, Y = np.meshgrid(x_vals, y_vals)
Z = X ** 2 + Y ** 2
    
ax.plot_surface(X, Y, Z, cmap = 'viridis', edgecolor = 'green')
ax.set_title('Surface Plot: z = x^2 + y^2')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.grid(True)
plt.show()


