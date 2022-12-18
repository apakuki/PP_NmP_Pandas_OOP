import matplotlib.pyplot as plt
import numpy as np
import math

# the input or x values
x = np.array([1, 2, 3, 4, 5, 6])
# f(x) = y
y = np.array([1, 3, 6, 7, 2, 1])

# the sin(x) function
x2 = np.arange(0, 2*math.pi, 0.01)
y2 = np.cos(x2)

plt.plot(x2, y2)
plt.show()