
# global variables
c = 10


def test_function():
    global c
    c = 15


test_function()
print(c)
