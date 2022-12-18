import numpy as np

a = np.array([[1, 2, 3], [7, 8, 9]])
b = np.array([[5, 6, 7], [10, 11, 12]])

# this is the so-called vstack()
result = np.vstack((a, b))

# hstack
result = np.hstack((a, b))

# stack function
result = np.stack((a, b), axis=1)
print(result)

