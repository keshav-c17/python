from collections import Counter
x = int(input()) #no. of shoes
a_shoe_size_ls = dict(Counter(list(map(int,input().split())))) #available shoe sizes
n = int(input()) #no. of customers
money_wallet = []


for i in range(n):
    d_shoe_size, price = map(int,input().split()) #desired shoe size
    if d_shoe_size in a_shoe_size_ls and a_shoe_size_ls[d_shoe_size] != 0:
        a_shoe_size_ls[d_shoe_size] -= 1
        money_wallet.append(price)
    else:
        continue

print(sum(money_wallet))





