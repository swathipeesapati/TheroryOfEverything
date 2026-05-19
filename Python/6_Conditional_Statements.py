# In this code snippet, we are working with conditional statements in Python.
# We will prompt the user to input a score, check if the score is within a valid
# range, and then determine the corresponding grade based on the score using 
# if-elif-else statements.

score = float(input("Enter Score: "))
if score >= 0.0 and score <= 1.0:
    if score >= 0.9:
        grade = 'A'
    elif score >= 0.8:
        grade = 'B'
    elif score >= 0.7:
        grade = 'C'
    elif score >= 0.6:
        grade = 'D'
    else:
        grade = 'F'
    print(grade)
else:
    print('wrong score')