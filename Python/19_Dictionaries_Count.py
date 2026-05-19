# In this code snippet, we are counting the occurrences of each name in a list

counts = dict()
names = ['swa','thi','Amar','Swa','thi']
for name in names:
    if name not in counts:
        counts[name] = 1
    else:
        counts[name] = counts[name] + 1
print(counts)
