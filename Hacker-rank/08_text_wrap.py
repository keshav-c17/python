import textwrap
s = "ABCDEFGHIJKLIMNOQRSTUVWXYZ"
wrapped = textwrap.wrap(s,4)
for i in wrapped:
    print(i)