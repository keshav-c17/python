s = input("Enter Full Name: ")

L = s.split(' ')
result_ls = []
for word in L:
    result_ls.append(word.capitalize())
print(' '.join(result_ls))




