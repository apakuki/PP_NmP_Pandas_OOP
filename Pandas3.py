import pandas as pd

d = {
    'Name': ['Adam', 'Joe', 'Daniel', 'Kevin', 'Ana'],
    'Age': [32, 56, 88, 38, 27]
}

df = pd.DataFrame(d, index=['p1', 'p2', 'p3', 'p4', 'p5'])

# column manipulation
# del df['Age']
df['New Age'] = 2 * df['Age']
print(df)

# row manipulation
# loc() - if we define the 'label' of the row
# iloc() - when we use the integer representation (it is FASTER)
# at() - specify the row and col index
# iat() - integer index of row and col (THIS IS THE FASTEST APPROACH)
print(df.iat[1, 1])