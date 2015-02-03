#https://projecteuler.net/problem=24
#solution 1: almost brute force utilise a combination of hand deduction and code computation. It's worth noticing that the number of 
#permutations is equal to the factorial of usable digits.So we find that the result should start with 27, then we retrieve all of the
# permulations and finally get the answer.

'''def dig2num(m,a,b,c,d,e,f,g,h,i):
	return m*10**9+a*10**8 + b*10** 7+ c*10**6 + d*10**5 + e*10** 4+f*10**3 +g*10**2 +h*10 + i
x = [0,1,3,4,5,6,8,9]
ans = set (dig2num(2,7,b,c,d, e, f, g, h, i) for b in x for c in x for d in x for e in x for f in x for g in x for h in x for i in x if len(set([b,c,d,e,f,g,h,i])) == 8)
ans = sorted(ans)
#print len(ans)
#print ans[32315:32325]
print ans[32319]'''

#solution 2:calculate each digit from the MSB to LSB based on the discovery that the number of permutations is equal to 
#the factorial of usable digits.
import math
def permu(x):
	d = range(10)
	rem = x-1
	i = 9
	result = 0
	while i >= 0:
		fac = math.factorial(i)	
		quo = rem / fac
		rem = rem % fac
		result += (d[quo]) * 10**i
		d.remove(d[quo])
		i -=1
	return result
print permu(1000000)
'''a =[]
for i in xrange(1,fac(10)+1):
	a = set(a.append(permu(i))'''
