import re

handle = open(r"C:\Users\swath\Documents\test.txt.txt")

total = 0

for line in handle:
    numbers = re.findall('[0-9]+', line)
    for num in numbers:
        total += int(num)

print(total)
