import matplotlib.pyplot as plt
import numpy as np

x = np.random.randint(100, size=1000)
y = np.random.randint(100, size=1000)
s = 3 * np.random.randint(100, size=1000)

plt.scatter(x, y, alpha=0.5, sizes=s, c=x+y, cmap='plasma')
plt.colorbar()
plt.show()