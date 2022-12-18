import numpy as np

# we can create a numpy array from a list
python_list = [1, 2, 3, 4]

numpy_array = np.array(python_list)

# we can store different types in Python BUT not with NumPy
a = np.array([1, 2, 3, 4, 5])
print(a)

# we can update the values based on indexes
a[1] = 10

# we can insert new items with the insert() function based on indexes
a = np.insert(a, 0, 30)
print(a)
