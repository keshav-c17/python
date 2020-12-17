n = int(input("Enter no. of english paper subscribers: "))
set_eng = set(map(int,input("Enter english set elements: ").split()))
b = int(input("Enter no. of french paper subscribers: "))
set_fre = set(map(int, input("Enter french set elements: ").split()))

total_subs_diff = set_eng ^ set_fre #set_eng.symmetric_difference(set_fre)
print(total_subs_diff)
print(len(total_subs_diff))