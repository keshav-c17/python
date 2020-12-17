S = input("Enter a String: ")
L_lower = []
L_upper = []
L_digit = []
L_alnum = []
for i in S:
    if i not in L_upper:
        if i not in L_lower:
            if i not in L_digit:
                if i not in L_alnum:
                    L_alnum.append(i.isalnum())
                L_digit.append(i.isdigit())
            L_lower.append(i.islower())
        L_upper.append(i.isupper())
print(any(L_alnum))

#Alphabet Check
alpha_lower = S.lower()
alpha_check = alpha_lower.islower()
print(alpha_check)

print(any(L_digit))
print(any(L_lower))
print(any(L_upper))








