# In this code snippet, we are working with string manipulation in Python.
# We will extract a specific portion of a string using the find method to locate
# the positions of certain characters and then slicing the string accordingly.

text = "X-DSPAM-Confidence:    0.8475"
pos = text.find('0')
spos = text.find('5',pos)
res = text[pos:spos+1]
print(res)