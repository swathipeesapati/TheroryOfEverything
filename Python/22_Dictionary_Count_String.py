count = dict()
print('Enter line')
line = input('')

words = line.split()
print('Words are : ', words)
print('Counting...')

for word in words:
    count[word] = count.get(word, 0) + 1
print(count)