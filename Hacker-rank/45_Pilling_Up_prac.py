from collections import deque
t = int(input())
for i in range(t):
    n = int(input())
    d = deque(map(int,input().split()))
    current_cube = d[0]
    for x in range(len(d)):
        left_most_cube, right_most_cube = d[0], d[-1]
        if left_most_cube >= right_most_cube:
            if current_cube >= left_most_cube or current_cube == d[0]:
                current_cube = left_most_cube
                d.popleft()
        elif current_cube >= right_most_cube or current_cube == d[0]:
            current_cube = right_most_cube
            d.pop()
    if len(d) == 0:
        print("Yes")
    else:
        print("No")





#or d[-1] >= d[i+1][:-1]