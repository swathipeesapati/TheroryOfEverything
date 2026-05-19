# In this code snippet, we are converting a floor number from the European system to the US system.
# In the European system, the ground floor is numbered 0, while in the US system,
# the ground floor is numbered 1. Therefore, to convert a European floor number 
# to a US floor number, we need to add 1 to the European floor number.

europeFloor = input('which floor?')
usFloor = int(europeFloor) + 1
print('floor in US is ', usFloor)