import pandas as pd
import numpy as np
import time

df = pd.DataFrame(np.random.rand(20000000, 5), columns=list('ABCDE'))

t = time.time()
# loc - deal with labels (it may return multiple values)
df.loc[np.random.randint(0, 20000000), 'A']
print('Time taken %.10fms' % (time.time()-t))

t = time.time()
# it is similar to loc - but here we have integer columns
df.iloc[np.random.randint(0, 20000000), 0]
print('Time taken %.10fms' % (time.time()-t))

t = time.time()
# it returns with a single value
df.at[np.random.randint(0, 20000000), 'A']
print('Time taken %.10fms' % (time.time()-t))

t = time.time()
# IT IS THE FASTEST APPROACH !!!
df.iat[np.random.randint(0, 20000000), 0]
print('Time taken %.10fms' % (time.time()-t))