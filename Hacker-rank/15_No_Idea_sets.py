n, m = map(int, input("Enter n and m: ").split())
arr = list(map(int,input("Enter elements of array: ").split()))
A = set(map(int, input("Enter setA elements: ").split()))
B = set(map(int, input("Enter setB elements: ").split()))


count = 0
for i in arr:
    if i in A:
        count += 1
    elif i in B:
        count -= 1
print(count)





