import math
AB = int(input("Enter side AB: "))
BC = int(input("Enter side BC: "))
MCB = round(math.degrees(math.atan(AB/BC)))
print(MCB)