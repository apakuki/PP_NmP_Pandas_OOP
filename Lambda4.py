
# standard functions can not be called immediately
# lambda expressions - immediately invoked function expressions (IIFEs)


def my_function(x):
    print(x)


my_function('This is the argument...')

print((lambda x, y: x + y)(25, 120))
