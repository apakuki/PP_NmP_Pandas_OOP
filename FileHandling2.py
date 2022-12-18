
# let's count the number of lines in a given file
# count the number of words in the text file
file = open('test_file', 'r')

word_counter = 0

for line in file:
    words = line.split()
    word_counter += len(words)

file.close()

print('The number of words is: ' + str(word_counter))
