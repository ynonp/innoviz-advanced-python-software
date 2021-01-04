# 1. Numpy is MUCH faster than normal lists
# 2. Numpy has many more options to create arrays

import numpy as np

# Create an array from data I have
a1 = np.array([10, 20, 30])

# Generate range data
a2 = np.arange(1, 100)

# Generate random data (ints)
a3 = np.random.randint(1, 100, size=100)

# Generate random data (floats)
a4 = np.random.rand(100)
a5 = np.linspace(1, 100)