import itertools
s = "1222311"

categorized = itertools.groupby(s)

for key,group in categorized:
    print((len(list(group)),int(key)),end=" ")

