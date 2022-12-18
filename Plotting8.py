import matplotlib.pyplot as plt
import numpy as np


# we have 5 wedges in this case
x = np.array([24, 10, 35, 23, 8])
labels = ['Tesla', 'BMW', 'Toyota', 'KIA', 'Ford']
# explode array (list)
explode_values = [0, 0, 0.1, 0, 0.1]
color_values = ['red', 'yellow', 'black', 'orange', 'green']

plt.pie(x, labels=labels, startangle=90, explode=explode_values, colors=color_values)
# python will show the labels as well
plt.legend(title='CAR BRANDS')
plt.show()
