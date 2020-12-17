from itertools import combinations
s,k = input().split()
s = "".join(sorted(s))

for i in range(1, int(k)+1):
    combos = combinations(s,i)
    for tupl in combos:
        print("".join(tupl))
