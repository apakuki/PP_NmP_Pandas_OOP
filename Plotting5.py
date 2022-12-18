import matplotlib.pyplot as plt
import numpy as np

x = np.array([1, 2, 3, 4, 5, 6])
y = np.array([1, 3, 6, 7, 2, 1])

# we will have 1 row and 2 cols (and actual one is the first one)
plt.subplot(2, 2, 1)
plt.plot(x, y)
plt.title('First plot')

# this is the second plot
plt.subplot(2, 2, 2)
plt.plot(y, x)
plt.title('Second plot')

# this is the third plot
plt.subplot(2, 2, 3)
plt.plot(y, x)
plt.title('Third plot')

# this is the fourth plot
plt.subplot(2, 2, 4)
plt.plot(y, x)
plt.title('Fourth plot')

plt.suptitle('MAIN TITLE')
plt.show()


