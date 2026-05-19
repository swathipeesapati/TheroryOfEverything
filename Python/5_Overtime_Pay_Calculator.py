# In this code snippet, we are creating an overtime pay calculator in Python.
# The program prompts the user to input the number of hours 
# worked and the pay rate per hour

hrs = int(input('Enter hours:'))
payPerHour = float(input('Pay Per Hour:'))
if hrs <= 40:
    pay = hrs * payPerHour
else:
    pay = (40 * payPerHour) + ((hrs-40) * (1.5 * payPerHour))
print(pay)
