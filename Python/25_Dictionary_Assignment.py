# 9.4 Write a program to read through the mbox-short.txt 
# and figure out who has sent the greatest number of mail messages. 
# The program looks for 'From ' lines and takes the second word of 
# those lines as the person who sent the mail. The program creates a 
# Python dictionary that maps the sender's mail address to a count 
# of the number of times they appear in the file. After the dictionary 
# is produced, the program reads through the dictionary using a 
# maximum loop to find the most prolific committer.
name = input("Enter file: ")
if len(name) < 1:
    name = "mbox-short.txt"

handle = open(name)

counts = dict()

# Read through the file line by line
for line in handle:
    # Look for lines that start with 'From '
    if line.startswith("From "):
        words = line.split()
        email = words[1]

        # Count occurrences of each email address
        counts[email] = counts.get(email, 0) + 1

# Find the email address with the highest count
bigcount = None
bigemail = None

for email, count in counts.items():
    if bigcount is None or count > bigcount:
        bigcount = count
        bigemail = email

print(bigemail, bigcount)