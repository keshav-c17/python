from itertools import permutations
S,k = "HACK 2".split()
L = sorted(list(permutations(S,int(k))))
print(L)
for tupl in L:
    for i in tupl:
        print(i,end="")
    print()
#METHOD-2
for tupl in L:
    print("".join(tupl))