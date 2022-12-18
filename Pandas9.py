import pandas as pd
import numpy as np
from time import time


df = pd.DataFrame(np.random.randint(0, 100, size=10000000), columns=['Number'])
df['Squared'] = ''

# let's calculate the square value of the numbers
start = time()
df['Squared'] = df['Number'].apply(lambda x: x**2)
print('Time taken with apply(): %.4fs' % (time() - start))

# vectorization (usually quite easy)
start = time()
df['Squared'] = df['Number'] ** 2
print('Time taken with vectorization: %.4fs' % (time() - start))


