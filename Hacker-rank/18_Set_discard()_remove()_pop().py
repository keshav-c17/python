n = int(input("Enter number of elements of set: "))
s = set(map(int, input("Enter elements of the set: ").split()))
N = int(input("Enter number of commands: "))
for i in range(N):
    command = input("Enter Command to be executed: ").split(" ")
    if command[0] == "pop":
        s.pop()
    elif command[0] == "remove":
        s.remove(int(command[1]))
    elif command[0] == "discard":
        s.discard(int(command[1]))
print(sum(s))






