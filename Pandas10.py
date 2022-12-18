import pandas as pd
import numpy as np
from time import time


def update_loop(data):
    for i in range(len(data)):
        if data['Age'][i] <= 11:
            data.at[i, 'Category'] = 'Child'
        elif data['Age'][i] > 11 and df['Age'][i] <= 18:
            data.at[i, 'Category'] = 'Teenager'
        elif data['Age'][i] > 18 and df['Age'][i] <= 65:
            data.at[i, 'Category'] = 'Adult'
        else:
            data.at[i, 'Category'] = 'Elderly'


# iterrows() is a bit better
# apply() is even better than iterrows() - it uses C implementation
def calculate_category(age):
    if age <= 11:
        return 'Child'
    elif 11 < age <= 18:
        return 'Teenager'
    elif 18 < age <= 65:
        return 'Adult'
    else:
        return 'Elderly'


def category_vectorized(data):

    conditions = [
        data['Age'] <= 11,
        data['Age'].between(12, 18),
        data['Age'].between(19, 65),
        data['Age'] > 65
    ]

    choices = ['Child', 'Teenager', 'Adult', 'Elderly']

    df['Category'] = np.select(conditions, choices, default='NaN')


df = pd.DataFrame(np.random.randint(0, 100, size=10000000), columns=['Age'])
df['Category'] = ''

start = time()
df['Category'] = df['Age'].apply(calculate_category)
print('Time taken with apply(): %.4fs' % (time() - start))

start = time()
category_vectorized(df)
print('Time taken with vectorization: %.4fs' % (time() - start))


