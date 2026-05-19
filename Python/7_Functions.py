# In this code snippet, we are defining a function called 'computepay' 
# that calculates the total pay based on hours worked and rate per hour. 
# The function takes into account overtime pay for hours worked over 40 hours. 
# We then prompt the user to input the hours and rate, call the function with 
# those inputs, and print the calculated pay.

def computepay(h, r):
    if hrs <= 40:
        pay = h * r
    else:
        pay = (40 * r) + ((h-40) * (1.5 * r))
    return pay

hrs = int(input("Enter Hours:"))
rph = float(input('Enter rate per hour:'))
p = computepay(hrs, rph)
print("Pay", p)