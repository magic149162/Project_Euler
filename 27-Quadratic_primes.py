#https://projecteuler.net/problem=29
#n=1 yields b, so b should be a prime.
#n=2 yields a+b+1, so a+b should be larger or equal to 1
#n**2+an+b = n(n+a)+b, when n is odd, to guarantee the sum is odd, a should be an odd number.
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
primes = filter(is_prime, xrange(2,1000)) 

'''with open('listprimes.txt','w') as f:
	for i in xrange(2,1100):
		if is_prime(i):
			f.write(str(i)+'\n')'''
a_max = 0
b_max = 0
n_max = 0

for b in primes:
	for a in xrange(-999,1000,2):
		if a+b < 1:
			continue
		n_temp = 0
		for n in xrange(b):
			#print n,a,b
			y=n**2+a*n+b
			if y <= 1:
				break
			elif not is_prime(y):
				break
			n_temp += 1
			if n_temp > n_max:
				n_max = n_temp
				a_max = a
				b_max = b
print n_max, a_max,b_max
print a_max*b_max
