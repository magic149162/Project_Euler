def is_abundant(x): 
	if sum(set([i for i in xrange(1,int(x**0.5+1)) if x%i==0] + [x/i for i in xrange(1,int(x**0.5+1)) if x%i==0] ))-2*x >0:
		return True
	else:
		return False
abu = [i for i in xrange(1,28124) if is_abundant(i)]

sum_list = set()

print len(abu)
#outer_loop = len([i for i in abu if i<=28124*0.5])

for i in xrange(0, len(abu)):
	for m in xrange(0,len(abu)):
		if (abu[i] +abu[m] < 28124):
			sum_list.add(abu[i] + abu[m])
	if (abu[i] < 14062):
		sum_list.remove(2*abu[i])

print sum(xrange(28124)) - sum(sum_list)

