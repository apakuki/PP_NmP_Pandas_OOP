
file = open('test_file', 'r')

# we are processing the file on a line by line basis
# for line in file:
#    print(line)

# we can process the file on a character by character basis
while True:

    actual_char = file.read(3)

    # we have reached the end of the file
    if not actual_char:
        break

    print(actual_char)

