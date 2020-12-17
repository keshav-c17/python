s = str(input("Enter String: "))
k = int(input("Enter number: "))

s_sgmnt_list = []
refined_list = []

for i in range(int(len(s)/k)):
    s_sgmnt_list.append(s[(k*i):(k*(i+1))])


for word in s_sgmnt_list:
    E_S = ''
    for letter in word:
        if letter not in E_S:
            E_S = E_S+letter
    refined_list.append(E_S)
for i in refined_list:
    print(i)







