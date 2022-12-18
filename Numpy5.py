import numpy as np

# reshape function changes the shape of a given array
# the shape is the number of items in each dimension

nums = np.array([1, 2, 3, 4, 5, 6])

print(nums)

# we can use -1 this is called "unknown" dimension - Python and NumPy will find the value
nums = nums.reshape(-1, 1)
print(nums)
