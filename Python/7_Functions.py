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