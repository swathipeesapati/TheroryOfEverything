# In this code snippet, we are performing various list manipulations in Python.
# We will concatenate two lists, slice a list, append an element to a list, 
# check for the presence of an element in a list, and calculate the average 
# of a list of numbers.

list_1 = ['a', 'b', 'c']
list_2 = ['d', 'a', 'f']

result = list_1 + list_2 #concatenation
print(result)

print(result[1:4]) #slicing

result.append('g') #append
print(result)

print('g' in result) #in operator # True
print('z' in result) #False

num_list = list() #creates empty list

num_list.append(1)
num_list.append(22)
num_list.append(44)

print(num_list)

print(sum(num_list)/len(num_list)) # average