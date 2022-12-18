
# string representation of objects


class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return '{%s, %s}' % (self.name, self.age)


p = Person('Kevin', 34)
print('The object is represented with the help of ' + str(p))
