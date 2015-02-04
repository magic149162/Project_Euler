#https://projecteuler.net/problem=10
def is_prime(x):
	is_prime = True
	if x <=1:
		#print x, "is not a prime."
		return False	
	for i in range(2,int(x**0.5+1),1):
		if (x % i ==0):
			is_prime = False
			break		
	if is_prime:
		#print x,"is a prime."
		return True
		#print x, "is not a prime."
		return False
def prime_in(x):
	return [2]+[i for i in range(3,x,2) if is_prime(i)]

print sum(prime_in(2000000))

'''sum = 2
for i in xrange(3,1999999,2):
	if is_prime(i): 
		sum += i
print sum'''
