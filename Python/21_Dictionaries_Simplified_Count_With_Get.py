# In this code snippet, we are counting the occurrences of each name in a list 
# of names.

counts = dict()
names = ['swa','thi','Amar','Swa','thi']
for name in names:
    counts[name] = counts.get(name, 0) + 1
print(counts)
