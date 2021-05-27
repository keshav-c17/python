a_dict = {'keshav': [10, 20, 30], 'kirtan': [20, 30, 40]}
qurey_name = input("Enter query name: ")

if qurey_name in a_dict:
    marks_for_avg = a_dict[qurey_name]

avg = sum(marks_for_avg)/len(marks_for_avg)
print(avg)



