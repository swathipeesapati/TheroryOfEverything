# In this code snippet, we are reading a file and extracting the email addresses
# from lines that start with "From". We will then print the email addresses and
# the total count.

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
