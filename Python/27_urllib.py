# urllib is a Python module that provides functions for working with URLs. 
# It allows you to open and read URLs, as well as parse and manipulate URL strings.
# In this example, we use urllib to open a URL and read its contents line by line.

import urllib.request, urllib.parse, urllib.error
fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
for line in fhand:
    print(line.decode().strip())