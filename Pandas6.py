import pandas as pd

# we have the valid data
df = pd.read_csv('info.txt', sep=',', names=['Name', 'Age'])
# axis=0 - rows
# axis=1 - columns
# df.dropna(axis=1, inplace=True)
df.fillna(10, inplace=True)
print(df)