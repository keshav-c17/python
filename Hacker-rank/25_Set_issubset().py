t = int(input("Enter no. of test cases: "))
for i in range(t):
    a = int(input("Enter no. of setA elements: "))
    A = set(map(int, input("Enter setA elements: ").split()))
    b = int(input("Enter no. of setB elements: "))
    B = set(map(int, input("Enter setB elements: ").split()))
    z = A.issubset(B)
    print(z)