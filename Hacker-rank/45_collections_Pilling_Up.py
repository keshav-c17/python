t = int(input())

for i in range(t):
    n = int(input())
    L = list(map(int,input().split()))
    min_term_index = L.index(min(L))
    left_ls = L[:min_term_index]
    right_ls = L[min_term_index+1:]
    if left_ls == sorted(left_ls, reverse=True) and right_ls == sorted(right_ls):
        print("Yes")
    else:
        print("No")