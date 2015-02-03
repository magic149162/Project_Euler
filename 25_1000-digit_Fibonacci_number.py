#https://projecteuler.net/problem=25
a,b=1,1
n = 2
while b < 10**999:
    a,b = b,a+b
    n += 1
print n