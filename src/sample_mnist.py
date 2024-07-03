# Import, minimize, and format data before testing to ensure proper implementation

import os
import gzip
import pickle
from matplotlib import pyplot as plt
import numpy as np

file_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'mnist.pkl.gz')

# Open and unpickle dataset
with gzip.open(file_path, 'rb') as f:
    data = pickle.load(f, encoding= "latin1")

(X_train, Y_train), (X_test, Y_test) = data

# Seperate out only first 1000 training examples
x_train = X_train[0:1000]
y_train = Y_train[0:1000]
x_test = X_test[0:100]
y_test = Y_test[0:100]

# Reshape into 2d matrix
x_train = x_train.reshape((1000, 784,)).T
x_test = x_test.reshape((100, 784,)).T

# Print test statements to confirm shape of each matrix
print(f"x_train shape: {x_train.shape}")
print(f"y_train shape: {y_train.shape}")
print(f"x_test shape: {x_test.shape}")
print(f"y_test shape: {y_test.shape}")
