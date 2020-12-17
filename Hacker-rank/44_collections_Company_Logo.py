from collections import OrderedDict
s = sorted(input())
s_sorted = "".join(s)
o_dict = OrderedDict()
for char in s_sorted:
    o_dict[char] = o_dict.get(char, 0) +1
sorted_dict = sorted(o_dict.items(), key=lambda item: item[1], reverse=True)
for tupl in sorted_dict[:3]:
    print(*tupl)


