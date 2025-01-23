import numpy as np
import matplotlib.pyplot as plt


def histogram_demo():
    data_normal = np.random.randn(300000)
    plt.figure(figsize = (6,4))
    plt.hist(data_normal, bins = 300, alpha = 0.7, color = 'green')
    plt.title('Histogram of normal distribution graph')
    plt.xlabel('Value')
    plt.ylabel('Frequency')
    plt.show()
    
    
def plot3d_demo():
    fig = plt.figure(figsize = (8, 6))
    ax = fig.add_subplot(111, projection = '3d')
    
    x_vals = np.linspace(-2, 2, 50)
    y_vals = np.linspace(-2, 2, 50)
    X, Y = np.meshgrid(x_vals, y_vals)
    Z = X ** 2 + Y ** 2
    
    ax.plot_surface(X, Y, Z, cmap = 'viridis', edgecolor = 'blue')
    ax.set_title('Surface Plot: z = x^2 + y^2')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.grid(True)
    plt.show()
    
    
if __name__ == "__main__":
    plot3d_demo()