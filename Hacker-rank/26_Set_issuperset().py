setA = set(map(int,input("Enter setA elements: ").split()))
n = int(input("Enter no. of other sets: "))
boolean_list = []
for i in range(n):
    test_set = set(map(int, input("Enter test set elements: ").split()))
    if setA == test_set or (setA.issuperset(test_set) is False):
        boolean_list.append(False)
    else:
        boolean_list.append(True)
x = all(boolean_list)

print(x)

