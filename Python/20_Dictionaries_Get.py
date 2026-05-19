#Get method is used to retrieve the value for a given key from a dictionary.
# If the key is not found in the dictionary, it returns a default value 
# (which is 0 in this case) instead of raising a KeyError.

counts = dict()
names = ['swa','thi','Amar','Swa','thi']
for name in names:
    if name not in counts:
        counts[name] = 1
    else:
        counts[name] = counts[name] + 1
name = 'Amar'
if name in counts:
    x = counts[name]
else:
    x = 0
x = counts.get(name, 0)

print(x)