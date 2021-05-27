#Creating a List(L) containing all the alphabets
import string
alphabets = string.ascii_lowercase
L = []
for i in alphabets:
    L.append(i)

n = int(input("Enter Size: "))

#Making the middle line of rangoli
x = '-'.join(L[n-1:0:-1]+L[:n])

#Middle line is the width of whole rangoli
Width = w = len(x)
#Upper Half
for i in range(1,n):
    print('-'.join(L[n-1:n-i:-1]+L[n-i:n]).center(w, '-'))
#Lower Half
for i in range(n,0, -1):
    print('-'.join(L[n - 1:n - i:-1] + L[n - i:n]).center(w, '-'))



