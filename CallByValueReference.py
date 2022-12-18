

# so because int, floats and strings are immutable objects in python - this is why
# we are not able to change the values

def change(x):
    x = 60.5


a = 30.5
change(a)
print(a)

# Python is able to change the values of mutable objects
# Python has something to do with "pass by object reference"


def add_item(l):
    l.append('This is a new item')


my_list = ['Kevin', 10, True]
add_item(my_list)
print(my_list)





