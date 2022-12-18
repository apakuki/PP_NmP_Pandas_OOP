
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# we would like to filter and get the items that are even
even_nums = list(filter(lambda x: x % 2 == 0, nums))

# we would like to filter and get the items that are even
odd_nums = list(filter(lambda x: x % 2 != 0, nums))
print(odd_nums)

# we can handle strings as well
names = ['Adam', 'Ana', 'Kevin', 'Daniel', 'Michael']

filtered_names = list(filter(lambda name: len(name) < 5, names))
print(filtered_names)

