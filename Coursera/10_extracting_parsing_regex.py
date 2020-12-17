import re
f_name = input("Enter filename: ")
f_handle = open(f_name)
digit_ls = re.findall('[0-9]+',f_handle.read())
converted_ls = []
for i in digit_ls:
    converted_ls.append(int(i))
print(sum(converted_ls))

