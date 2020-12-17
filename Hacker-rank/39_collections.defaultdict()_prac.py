from collections import defaultdict
A = [None]
B = [None]
result_dict = defaultdict(set)
n,m = map(int, input().split())
for i in range(n):
    A.append(input())
for j in range(m):
    B.append(input())
for index in range(len(A)):
    for char in B:
        if A[index] == char:
            result_dict[char].add(index)
        elif char not in A:
            result_dict[char].add(-1)
del result_dict[None]
for char,index in result_dict.items():
    print(*(index)