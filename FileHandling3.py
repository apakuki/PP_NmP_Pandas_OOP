
# count occurrences of given words in a text file

file = open('test_file', 'r')

counter = 0

for line in file:
    words = line.split()
    counter += len([word for word in words if word.lower() == 'first'])

file.close()

print('The number of occurrences: ' + str(counter))
