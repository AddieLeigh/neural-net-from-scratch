#Demonstrates module matplotlib's scatter plot and labelling functionalities using GUI backend tkinter

import matplotlib

from matplotlib import pyplot as plt

matplotlib.use("TkAgg")
x_values = [1, 2, 3, 4]
y_values = [5, 39, 2, 20]

plt.scatter(x_values, y_values)
plt.title("Sample Scatter Plot")
plt.xlabel("X-values")
plt.ylabel("Y-values")

plt.show()
