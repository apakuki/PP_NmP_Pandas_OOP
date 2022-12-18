
# lambda functions - anonymous functions
# we can check the traceback


def my_function(x):
    return x / 0


# so lambda functions are very similar to functions BUT they are not functions
my_lambda = lambda x: x / 0


print(my_lambda(10))
