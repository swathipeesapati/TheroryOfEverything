my_list = ['a','b','c','d']
print(len(my_list))
print(list(range(len(my_list))))
print(list(range(4)))

# counted loop
for i in range(len(my_list)):
    letter = my_list[i]
    print('Hi', letter)


for letter in my_list:
    print('Hi', letter)