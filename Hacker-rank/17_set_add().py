n = int(input("Enter no. of countries: "))
list_of_countries = set()
for i in range(n):
    list_of_countries.add(str(input("Enter names of the countries: ")))
print(len(list_of_countries))

