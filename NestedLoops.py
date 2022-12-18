
# we can use multiple loops inside other loops - and these are called nested loops

for outer_index in range(5):
    for inner_index in range(3):
        print('outer_index: ' + str(outer_index) + ' inner_index: ' + str(inner_index))
