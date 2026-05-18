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