# In this code snippet, we are working with the range function in Python.
# We will create a list of letters and use the range function to iterate over the indices of the list.

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