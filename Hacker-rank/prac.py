from itertools import permutations
S,k = "HACK 2".split()
L = sorted(list(permutations(S,int(k))))
print(L)


for tupl in L:
    print("".join(tupl))


