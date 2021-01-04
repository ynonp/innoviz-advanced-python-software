import numpy as np

# Create a 3d array
a1 = np.arange(27).reshape(3, 3, 3)

# Create a nd array
a2 = np.array([
    [' ', ' ', ' '],
    ['X', 'O', 'X'],
    ['O', ' ', ' '],
])

print(a1)
print(a2[1, 1])
print(a1[0, 1, 2])
