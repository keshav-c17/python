name_lst = list()
score_lst = list()
combo_lst = list()
if __name__ == '__main__':
    for student in range(int(input("Enter Number of Students: "))):
        name = input("Enter Name: ")
        name_lst.append(name)
        score = float(input("Enter Score: "))
        score_lst.append(score)
        merged_lst = combo_lst.append([name_lst[student], score_lst[student]])
        combo_lst.sort(key=lambda x: x[1])
for i in range(0,len(combo_lst)):
    second_low = 0
    if combo_lst[i][1] != combo_lst[0][1]:
        second_low = combo_lst[i][1]
        break
#print(second_low)
for x in combo_lst:
    if x[1] == second_low :
        sec_low_student = [x[0]]
sec_low_student.sort()
for s_name in sec_low_student:
   print(s_name)