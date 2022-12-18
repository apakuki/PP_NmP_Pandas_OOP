

# define a function that increments the argument by 10
def increment_normal(x):
    return x + 10


# let's apply lambda expressions
increment_lambda = lambda x, y, z: x * y * z


print(increment_lambda(5, 10, 3))
