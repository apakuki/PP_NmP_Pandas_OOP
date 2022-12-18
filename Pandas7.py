import pandas as pd
import numpy as np


# using loops is the slowest approach !!! (loc)
# iterrows() but it still not tha efficient
# apply() function is quite fast (C code)
def calculate_category(age):
    if age <= 11:
        return 'Child'
    elif 11 < age <= 18:
        return 'Teenager'
    elif 18 < age <= 65:
        return 'Adult'
    else:
        return 'Elderly'


df = pd.DataFrame(np.random.randint(0, 100, size=10), columns=['Age'])
df['Category'] = ''

df['Category'] = df['Age'].apply(calculate_category)
print(df)

