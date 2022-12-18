
def sorted_logic(x):
    return len(x)


# natural ordering [1, 5, 3, -5] - [-5, 1, 3, 5]

nums = [10, -5, 0, 4, 8, -9, 34, 100]

# sorted function always return a list
# descending order - reverse
result = sorted(nums, reverse=True)

names = ['Adam', 'Kevin', 'Ana', 'Joe', 'Daniel', 'Michael']
names = sorted(names, reverse=True)
print(names)

# sorted function has the KEY parameter - we can define the logic behind sorting
# let's sort names based on the length of the strings

texts = ['This', 'This is a ', 'T', 'This is the longest string', 'This is the second...']

texts = sorted(texts, key=len, reverse=True)

# what if we want to sort dicts


def dict_sorter(x):
    return x[1]


people = {'Adam Smith': 34, 'Albert Camus': 56, 'Kurt Godel': 45, 'Jean-Paul Sartre': 31}

result = sorted(people.items(), key=dict_sorter, reverse=True)
print(result)
