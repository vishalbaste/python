import numpy as np

my_array = np.array([[1, 2],
                     [3, 4]])

my_array = np.genfromtxt('data.csv', delimiter=',', dtype=None, names=True)

# Compute the sum of each column
column_sums = np.sum(my_array, axis=0)
column_means = np.mean(my_array, axis=0)
column_means = np.median(my_array, axis=0)
column_means = np.max(my_array, axis=0)