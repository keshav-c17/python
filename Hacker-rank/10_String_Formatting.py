#n = int(input("Enter Number: "))
#for i in range(1,n+1):
#    print(str(i).rjust(4), end=" ")
#    print(oct(i)[2:].rjust(4), end=" ")
#    print(hex(i)[2:].upper().rjust(4), end=" ")
#    print(bin(i)[2:].center(4," "))
def print_formatted(number):
    width = len(bin(n)[2:])

    for i in range(1,n+1):

        print(str(i).rjust(width), end=" ")
        print(oct(i)[2:].rjust(width), end=" ")
        print(hex(i)[2:].upper().rjust(width), end=" ")
        print(bin(i)[2:].rjust(width))
    return


if __name__ == '__main__':
    n = int(input("Enter Number: "))
    print_formatted(n)


