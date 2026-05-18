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