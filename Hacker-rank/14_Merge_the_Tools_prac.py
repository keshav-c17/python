list_of_words = ['ABCD', 'BDBD', 'KLKL','BDEE']

result = []

for word in list_of_words:
    E_S = ''
    for letter in word:
        if letter not in E_S:
            E_S = E_S+letter
    result.append(E_S)
print(result)






























