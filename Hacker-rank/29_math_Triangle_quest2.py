import math
N= int(input("Enter integer: "))
for i in range(1,N+1):
    print(math.trunc(math.pow(10,i)/9)**2)
#without math module
for i in range(1,int(input("Enter integer (part 2): "))+1):
    print(round(((10**i)/9))**2)