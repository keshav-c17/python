string = input("Enter String: ")
length = len(string)

#Creating a list of sub-strings from the given string
sub_string_ls = []
for i in range(length):
    for j in range(i,length):
        sub_string_ls.append(string[i:j + 1])

#Dividing the sub-strings into kevin and stuart
vowels = "AEIOU"
stuart_list = []
kevin_list = []
for i in sub_string_ls:
    for vowel in vowels:
        if i.startswith(vowel):
            kevin_list.append(i)
for i in sub_string_ls:
    for word in kevin_list:
        if word in sub_string_ls:
            sub_string_ls.remove(word)

#Creating the dictionary
kevin_dict = {}
stuart_dict = {}
for i in kevin_list:
    kevin_dict[i] = kevin_list.count(i)
for i in sub_string_ls:
    stuart_dict[i]= sub_string_ls.count(i)

#Calculating the scores using dictionary
kevin_score = sum(kevin_dict.values())
stuart_score = sum(stuart_dict.values())

#Comparing and calculating winner
if kevin_score > stuart_score:
    print("Kevin",kevin_score)
elif kevin_score < stuart_score:
    print("Stuart", stuart_score)
elif kevin_score == stuart_score:
    print("Draw")

#print(kevin_list)
#print(sub_string_ls)
#print(kevin_dict)
#print(stuart_dict)