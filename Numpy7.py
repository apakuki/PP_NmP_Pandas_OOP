import numpy as np

# filtering

a = np.array([1, 2, 3, 4, 5, 6, 7, 8])
boolean_array = [True, True, False, False, True, False, True, False]

# result = a[boolean_array]

result = a % 2 != 0

print(a[result])
