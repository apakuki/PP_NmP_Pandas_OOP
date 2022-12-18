
def operation(x):

    # the x value is even
    if x % 2 == 0:
        return True, 1, 'this is a string'

    return False, -1


b, v, s = operation(10)
print(b)
print(v)
print(s)
