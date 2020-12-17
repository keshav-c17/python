from itertools import product
A = list(map(int,input("Enter A elements: ").split()))
B = list(map(int,input("Enter B elements: ").split()))
AxB = sorted(list(product(A,B)))
print(*AxB,sep=" ")
