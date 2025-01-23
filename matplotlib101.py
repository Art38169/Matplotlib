import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-10, 10, 400)  # 400 points from -10 to 10

y = x ** 2
y1 = x * np.sin(2 * x)
y2 = np.arctan(x)

plt.plot(x, y, color = 'Green')
plt.plot(x, y1, color = 'Red', linestyle = 'dashed')
plt.plot(x, y2, color = 'Yellow', linestyle = 'dotted')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Graph of x^2, xsin(2x), arctg(x)')
plt.legend()
plt.grid(True)


plt.show()
