from functools import reduce

original_values = [1, 2, 3, 4, 5]

# use the reduce function to sum up the values
result = reduce(lambda x, y: x + y, original_values)

# use the reduce function to multiply the values
result_multiply = reduce(lambda x, y: x * y, original_values)

# use the reduce function with strings
names = ['Adam', 'Kevin', 'Joe']

result_name = reduce(lambda name1, name2: name1[0] + name2[0], names)

# let's calculate the min and max values

values = [1, -5, 10, 450, 23, 99, -34]

min_value = reduce(lambda x, y: x if x < y else y, values)
max_value = reduce(lambda x, y: y if x < y else x, values)

print(max_value)
