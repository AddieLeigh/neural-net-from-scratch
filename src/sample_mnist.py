# Setup preliminary imports and test that dataset is correctly imported

import os
import gzip
import pickle
from matplotlib import pyplot as plt
import numpy as np

file_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'mnist.pkl.gz')

# Open and unpickle dataset
with gzip.open(file_path, 'rb') as f:
    data = pickle.load(f, encoding= "latin1")

(x_train, y_train), (x_test, y_test) = data

# Print test statements to confirm shape of each matrix
print(f"x_train shape: {x_train.shape}")
print(f"y_train shape: {y_train.shape}")
print(f"x_test shape: {x_test.shape}")
print(f"y_test shape: {y_test.shape}")
