n = int(input("Enter no. of elements: "))
A = set(map(int, input("Enter elements of the setA: ").split()))
N = int(input("Enter no. of other sets: "))
for i in range(N):
    command = input("Enter command: ").split()
    if command[0] == "intersection_update":
        tempIU = set(map(int, input("Enter elements of tempIU: ").split()))
        A.intersection_update(tempIU)
    elif command[0] == "update" :
        tempU = set(map(int, input("Enter elements of tempU: ").split()))
        A.update(tempU)
    elif command[0] == "symmetric_difference_update":
        tempSDU = set(map(int, input("Enter elements of tempSDU: ").split()))
        A.symmetric_difference_update(tempSDU)
    elif command[0] == "difference_update":
        tempDU = set(map(int, input("Enter elements of tempDU: ").split()))
        A.difference_update(tempDU)

print(sum(A))