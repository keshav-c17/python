S = input("Enter a String: ")

#Alphnumeric Check
L_alnum = []
for i in S:
    if i not in L_alnum:
        L_alnum.append(i.isalnum())
print(any(L_alnum))

#Alphabet Check
alpha_lower = S.lower()
alpha_check = alpha_lower.islower()
print(alpha_check)

#Digit Check
L_digit = []
for i in S:
    if i not in L_digit:
        L_digit.append(i.isdigit())

print(any(L_digit))

#Lowercase Check
L_lower = []
for i in S:
    if i not in L_lower:
        L_lower.append(i.islower())
print(any(L_lower))

#Uppercase Check
L_upper = []
for i in S:
    if i not in L_upper:
        L_upper.append(i.isupper())
print(any(L_upper))







#L = []
#for i in S:
#    if i not in L:
#        L.append(i)
#for char in L:
#    if char.isalnum() and char.isdigit():
#        print("True")
#    else:
#        print("False")





