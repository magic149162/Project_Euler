#https://projecteuler.net/problem=23
# solution 1: use double loops to acquire a set of the sum of 2 abundant numbers under upper limit. It takes about 12s.
'''
def is_abundant(x): 
	if sum(set([i for i in xrange(1,int(x**0.5+1)) if x%i==0] + [x/i for i in xrange(1,int(x**0.5+1)) if x%i==0] ))-2*x >0:
		return True
	else:
		return False
abu = [i for i in xrange(1,28123) if is_abundant(i)]

sum_list = set()
outer_loop = len([i for i in abu if i< 28123*0.5])

#considering 28123 is set as an upper limit for non-abundant number, and the sum of 2 abundant numbers 
#both more than a half of 28123 will definitely exceed the limit, we can decrease the iterative times of the outer loop.
for i in xrange(0, outer_loop):
	for m in xrange(0, len(abu)):
		if (abu[i] +abu[m] < 28123):
			sum_list.add(abu[i] + abu[m])
print sum(xrange(28123)) - sum(sum_list)'''


#soulition 2: utilise list comprehension to generate a set to store the sum of 2 abundant numbers, and then compute difference 
#between complete set and the set. It takes about 4s to get the answer
def is_abundant(x): 
	if sum(set([i for i in xrange(1,int(x**0.5+1)) if x%i==0] + [x/i for i in xrange(1,int(x**0.5+1)) if x%i==0] ))-2*x >0:
		return True
	else:
		return False
abu = [i for i in xrange(1,28123) if is_abundant(i)]

outer_loop = len([i for i in abu if i< 28123*0.5])

#considering 28123 is set as an upper limit for non-abundant number, and the sum of 2 abundant numbers 
#both more than a half of 28123 will definitely exceed the limit, we can decrease the iterative times of the outer loop.
sum_list = set(i+j for i in abu[:outer_loop] for j in abu)
print sum(set(xrange(28123)) - sum_list)
