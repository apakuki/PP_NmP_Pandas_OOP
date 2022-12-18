
def int_multiply(x):
    return lambda c: c * x


int_double = int_multiply(2)
int_triple = int_multiply(3)
int_tenfold = int_multiply(10)

print(int_tenfold(100))
print(int_tenfold(50))
print(int_tenfold(40))
