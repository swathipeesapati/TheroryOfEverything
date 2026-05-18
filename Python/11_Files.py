fhand = open('C:\\Users\\swath\\Documents\\Career\\Python\\sample_text.txt')
count = 0
for line in fhand:
    line = line.rstrip() #every line in the file will have a hidden new line character and print in python will always print in new line. 
    #this will create extra new line which is an empty lune. So always strip it
    print(line)
    count = count + 1
print(count)


#with proper exception handling
try:
    fhand = open('C:\\Users\\swath\\Documents\\Career\\Python\\sampletext.txt')
except:
    print('Invalid File name')
    quit()
count = 0
for line in fhand:
    line = line.rstrip()
    print(line)
    count = count+1
print(count)
