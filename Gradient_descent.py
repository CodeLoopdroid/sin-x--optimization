import numpy as np
import matplotlib.pyplot as plt

def function(x):
    return np.sin(x)

def derivative(x):
    return np.cos(x)

x_values = np.arange(-8 * np.pi, 8 * np.pi, 0.1)
y_values = function(x_values)

current_point = (np.pi / 4, function(np.pi / 4))

learning_rate = 0.1
iterations = 1000

for _ in range(iterations):
    new_x = current_point[0] - learning_rate * derivative(current_point[0])
    new_y = function(new_x)
    current_point = (new_x, new_y)
    
    plt.plot(x_values, y_values, color="black")
    plt.scatter(current_point[0], current_point[1], color='red')
    plt.title(f"x = {current_point[0]:.4f}, y = {current_point[1]:.4f}")
    plt.pause(0.01)
    plt.clf()
