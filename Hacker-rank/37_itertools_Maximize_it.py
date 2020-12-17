import itertools
k,m = map(int,input().split())
L= []
result_L = []
for i in range(k):
    L.append(list(map(int, input().split()))[1:])
product_combos = list(itertools.product(*L))
print(product_combos)
for tupl in product_combos:
    tupl_sum_sqr = 0
    for i in tupl:
        tupl_sum_sqr += i**2
    result_L.append(tupl_sum_sqr%m)
print(max(result_L))

