# In this code snippet, we are calculating the pay for an employee based 
# on the number of hours worked and the pay rate per hour. 
# The program prompts the user to input the hours and pay rate, 
# performs the calculation, and then prints the total pay.

hrs = input('Enter hours:')
payPerHr = input('Enter Pay per hour:')
pay = int(hrs) * float(payPerHr)
print('Pay:', pay)