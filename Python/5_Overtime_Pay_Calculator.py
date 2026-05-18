hrs = int(input('Enter hours:'))
payPerHour = float(input('Pay Per Hour:'))
if hrs <= 40:
    pay = hrs * payPerHour
else:
    pay = (40 * payPerHour) + ((hrs-40) * (1.5 * payPerHour))
print(pay)
