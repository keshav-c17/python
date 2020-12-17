k,m = map(int, input("Enter K and M: ").split())
large_num_ls = []
large_num = None
large_mod = None
for i in range(k):
    L = list(map(int, input("Enter elements of lists").split()))
    L.pop(0)
    for num in L:
        tempdict = {}
        tempdict[num] = num % m
        for d_num, mod in tempdict.items():
            if large_mod is None or mod >= large_mod:
                large_num = d_num
                large_mod = mod
    large_num_ls.append(large_num**2)

print(sum(large_num_ls)%m)


##Code to find largest number in a list

#num = None
#for i in L:
#    if num is None or i > num:
#        num = i
#print(num)