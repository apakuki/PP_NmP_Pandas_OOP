import matplotlib.pyplot as plt
import numpy as np

x = np.array(['A', 'B', 'C'])
y = np.array([13, 22, 9])

plt.bar(x, y, color='blue', width=0.2)
plt.title('Bar Chart')
plt.xlabel('Letters')
plt.ylabel('Frequency')
plt.show()
