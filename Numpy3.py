import numpy as np

nums = np.array([[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]])

# negative indexes represent indexes starting from the last item
print(nums[1][2])

# we can use slicing with :
# print(nums[::-1])
