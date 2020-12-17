m = int(input("Enter m:"))
M = set(map(int, input("Enter setM elements: ").split()))
n = int(input("Enter n: "))
N = set(map(int, input("Enter setN elements: ").split()))
symmetric_diff_N = N.difference(M)
symmetric_diff_M = M.difference(N)
union_sets = symmetric_diff_M.union(symmetric_diff_N)
union_sets_list = sorted(union_sets)

for i in union_sets_list:
    print(i)


