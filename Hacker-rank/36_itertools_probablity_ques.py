import itertools
n = int(input("Enter no. of elements of list: "))
list_elemnts = list(map(str,input("Enter elements of the list: ").split()))
k = int(input("Enter no. of indices to be picked: "))

x = list(itertools.combinations(list_elemnts,k))
count = 0
length = len(x)
for tupl in x:
    if "a" in tupl:
        count+= 1
print(round((count/length),4))