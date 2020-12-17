from collections import defaultdict
n,m = map(int,input().split())
result_dict = defaultdict(list)
B = []
for i in range(1, n+1):
    result_dict[input().rstrip()].append(i)
for j in range(m):
    B.append(input())

for char in B:
    if char in result_dict.keys():
        print(*result_dict[char])
    else:
        print(-1)