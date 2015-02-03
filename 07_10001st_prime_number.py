#https://projecteuler.net/problem=7
from math import sqrt
def is_prime(x):
	is_prime = True
	for i in range(2,int(round(sqrt(x)+1)),1):
		if (x % i ==0):
			is_prime = False
			break
	if is_prime:
		#print x,"is a prime."
		return True
	else:
		#print x, "is not a prime."
		return False
def prime_in(x):
	return [2]+[i for i in range(3,x,2) if is_prime(i)]

l = prime_in(110000)
print l[10000]
