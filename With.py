
# with keyword - we can simplify try-except-finally blocks

try:

    # so we do not have to close the file resource
    with open('test_fil', 'r') as file:
        for line in file:
            print(line)

except FileNotFoundError:
    print('We have managed to catch an Error...')



