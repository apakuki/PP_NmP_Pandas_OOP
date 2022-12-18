import pandas as pd

# Series - one-dimensional data (single column)
s = pd.Series([10, 20, 30, 40], index=['a', 'b', 'c', 'd'])

s['a'] = 100

# print(s[['a', 'd']])

populations = [1000, 4500, 300, 100]
countries = ['France', 'USA', 'Germany', 'UK']

s2 = pd.Series(populations, index=countries)
print(s2.mean())