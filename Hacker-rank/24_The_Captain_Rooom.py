k = int(input("Enter no. of members per group: "))
room_no_list = list(map(int, input("Enter room numbers: ").split()))
unique = set()
repeating = set()

for room_no in room_no_list:
    if room_no not in unique:
        unique.add(room_no)
    else:
        repeating.add(room_no)
print(unique)
print(repeating)
print((unique - repeating).pop())
