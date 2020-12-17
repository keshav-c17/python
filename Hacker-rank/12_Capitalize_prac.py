def solve(s):
    L = s.split()
    # if L[0].isalnum() and L[1].isalnum() is True:
    # L = s.split()
    First_nam = str(L[0].capitalize())
    Last_nam = str(L[1].capitalize())
    print(First_nam, Last_nam)
s = input("Enter Name: ")
result = solve(s)