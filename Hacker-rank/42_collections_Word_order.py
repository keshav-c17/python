from collections import OrderedDict
n = int(input())
O_dict = OrderedDict()
for i in range(n):
    word = str(input())
    O_dict[word] = O_dict.get(word, 0) +1
print(len(O_dict))
for key,value in O_dict.items():
    print(value, end=" ")
