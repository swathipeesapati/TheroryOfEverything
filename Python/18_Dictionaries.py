# A dictionary in Python is a collection of key-value pairs.
# Each key is unique and maps to a value.
# In this code snippet, we are creating a dictionary called 'my_dict' and adding some key-value pairs to it. 
# We then print the dictionary, retrieve a value using a key, update a value, and check for the presence of keys in the dictionary.
my_dict = dict()
my_dict['a'] = 1
my_dict['b'] = 3
my_dict['d'] = 44

print(my_dict)

print(my_dict['d'])

my_dict['a'] = my_dict['b'] + my_dict['d']
print(my_dict['a'])
print(my_dict)

# in is used to verify if the key is present in dict
print('a' in my_dict)
print('c' in my_dict)