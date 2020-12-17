import cmath

c = complex(input("Enter complex num: "))
r = abs(c)
phase = cmath.phase(c)
print(r)
print(phase)
