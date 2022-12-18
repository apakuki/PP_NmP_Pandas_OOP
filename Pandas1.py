import pandas as pd

my_dict = {
    'name': ['Adam', 'Joe', 'Kevin'],
    'age': [12, 66, 34]
}

df = pd.DataFrame(my_dict)
print(df)