
class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __ne__(self, other):
        return self.name < other.name


# how to compare the objects?
p1 = Person('Joe', 88)
p2 = Person('Adam', 56)

# we can override the standard functions
# __eq__ this is the built-in function to decide whether 2 objects are the same or not
print(p1 != p2)
