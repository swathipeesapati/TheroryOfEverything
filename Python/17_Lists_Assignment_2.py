fname = input("Enter file name: ")
if len(fname) < 1:
    fname = "mbox-short.txt"

fh = open(fname)
count = 0
lst = list()

for line in fh:
    if(line.startswith("From")):
        words = line.split()
        lst.append(words[1])
for item in lst:
    print(item)
    
print(len(lst))
