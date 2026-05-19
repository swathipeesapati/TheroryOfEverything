# In this code snippet, we are demonstrating string conversion in Python.
# We will take a string that represents a number, convert it to an integer, 
# and then perform a simple arithmetic operation. We will also show what happens
# when we try to convert a non-numeric string to an integer, which will result 
# in an error.

sval = '123'
ival = int(sval)
print(ival + 1) # prints 124

sval = 'abc'
ival = int(sval) # throws error
print(ival + 1)
