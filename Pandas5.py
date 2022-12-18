import pandas as pd

# df = pd.read_csv('TSLA.csv', skiprows=1, names=['A', 'B', 'C', 'D', 'E', 'F', 'G'], index_col='A')
# df = pd.read_csv('info.txt', sep=' ', names=['Name', 'Age'])
df = pd.read_csv('TSLA.csv')
print(df.corr())