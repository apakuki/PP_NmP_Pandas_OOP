
nums = [1, 2, 3, 4, 5, 6]

# increment the values of these numbers
incremented_nums = list(map(lambda num: num * num, nums))

print(incremented_nums)

# map function can handle strings as well

names = ['Adam', 'Ana', 'Kevin', 'Joe', 'Daniel']

transformed_names = list(map(lambda name: len(name), names))
print(transformed_names)

# we can use the map function with multiple data structures

nums1 = [1, 2, 3]
nums2 = [5, 6, 7, 8]

merged_nums = list(map(lambda x, y: x * y, nums1, nums2))
print(merged_nums)
