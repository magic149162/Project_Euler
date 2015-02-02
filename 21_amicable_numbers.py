#Evaluate the sum of all the amicable numbers under 10000
#solution 1: less time but more lines
'''def d(x):
	d = set()
	if x == 1:
		return d
	for i in xrange(1,int(x**0.5+1)):
	 	m = x % i
	 	n = x / i
	 	if m == 0 :
	 		d.add(i)
	 		d.add(n)
	d.remove(x)
	return sum(d)	
ami = []
for a in xrange(2, 10000,1):
	b = d (a)
	if d(b) == a and a != b:
		ami.extend([a,b]) 
print sum(set(ami))'''

#solution 2: less lines than solution 1 but a little bit more time.

'''def d(x):
	#One list to store divisors and the other  to store quotients. Be aware to remove repeat numbers  and x itself.
	return sum(set([i for i in xrange(1,int(x**0.5+1)) if x%i==0] + [x/i for i in xrange(1,int(x**0.5+1)) if x%i==0] ))-x
amic_d = {i:d(i) for i in xrange(1,10000)}
#a and b are amicable pairs under the condition that both d(a) = b , d(b) = a and a! = b.
print sum(i for i in xrange(1,10000) if amic_d.get(d(i)) == i and d(i) != i)'''

#solution 3: an approriate balance between type work and running time
def d(x): return sum(set([i for i in xrange(1,int(x**0.5+1)) if x%i==0] + [x/i for i in xrange(1,int(x**0.5+1)) if x%i==0] ))-x
print sum(i for i in xrange(1,10000) if d(d(i)) == i and i != d(i))

#solution 4:leat lines but longest time
'''def d(x): return sum(i for i in xrange(1,int(x*0.5+1)) if x%i==0)
print sum(i for i in xrange(1,10000) if d(d(i)) == i and i != d(i))'''
