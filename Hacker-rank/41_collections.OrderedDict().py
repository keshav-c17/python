from collections import OrderedDict
n = int(input())
O_dict = OrderedDict()
for i in range(n):
    item_name_price = input().split()
    item_name = " ".join(item_name_price[:-1])
    price = int(item_name_price[-1])
    O_dict[item_name] = O_dict.get(item_name, 0) + price
for key,value in O_dict.items():
    print(key, value)


