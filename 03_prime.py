#https://projecteuler.net/problem=3
#find the largest primate below a certain number
"""def prim(x):
	i=x
	state = "f"
	while True:
		i-=1
		j=2
		while (j<=round(i**0.5+1)):
			if(i%j==0):
				if(i==3):
					print "3 is the largest primate below ",x
					state = "Found"
					break
				elif(i==2):
					print "2 is the largest primate below ",x
					state = "Found"
					break
				else:
					break
#			else:
#				print i,j
#				print round(i**0.5+2)
#				j+=1
			elif(j==round(i**0.5+1)):
				state = "Found"
				print i, "is the largest primate below",x
				break
			else:
				j+=1
		if(state == "Found"):
			break
prim(600851475143)"""

'''
#find the largest primate below a certain number
def prim(x):
	i=x
	k=2
	while True:
		i-=1
#		print "i=",i
		j=2
		while (j<=round(i**0.5+1)):
			if(i%j==0):
#				print i,j
				if(i==3):
					print "3 is a primate below ",x
#					state = "Found"
					break
				elif(i==2):
					print "2 is a primate below ",x
#					state = "Found"
					break
				else:
					break
#			else:
#				print i,j
#				print round(i**0.5+2)
#				j+=1
			elif(j==round(i**0.5+1)):
#				state = "Found"
				print i, "is a primate below",x
				k=i
				break
			else:
				j+=1
		if(not x%k):
			print "The largest primate factor of {} is {}".format(x, i)
			break
prim(600851475143)'''

#check if an integer is a prime.
from math import sqrt
def is_prime(x):
	is_prime = True
	for i in range(2,int(round(sqrt(x)+1)),1):
		if (x % i ==0):
			is_prime = False
			break
	if is_prime:
		print x,"is a prime."
		return True
	else:
		print x, "is not a prime."
		return False



from math import sqrt
def prime_factor(x):
	primes = [2]
	factors = []
	if (x%2 == 0):factors.append(2)
	value = 3
	number = x
	#number = 600851475143
	#number = 600851475067
	while value < sqrt(number)+1:
	    isPrime = True
	    for k in primes:
	        if value % k == 0:
	            isPrime = False
	            value += 2
	    if isPrime:
	        primes.append(value)
	        if number % value == 0:
#	            print value
	            factors.append(value)
	            number /= value
	            value = value+2
	if(number == x):
		print "cannot find primate factors, as {} itself is a primate number ".format(x)
	else:
		factors.append(number)
		print "The largest primate factor of {} is {}".format(x,number)
#error		print "The primate numbers below {} are listed as follows:\n{}".format(x,primes)
		print "The primate factors of {} are listed as follows:\n{}".format(x,factors)
ans=prime_factor(600851475143)
ans=prime_factor(10000)
