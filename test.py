import numpy as np
import matplotlib.pyplot as plt


def histogram_demo():
    data_normal = np.random.randn(1000)
    plt.figure(figsize = (6,4))
    plt.hist(data_normal, bins = 30, alpha = 0.7, color = 'green')
    plt.title('Histogram of normal distribution graph')
    plt.xlabel('Value')
    plt.ylabel('Frequency')
    plt.show()
    
if __name__ == "__main__":
    histogram_demo()