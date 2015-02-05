#https://projecteuler.net/problem=30

#solution 1
#caculate for a given number x, sumation of each digit to the 4th power
def p5_sum(x):
	p5_sum = 0
	for i in str(x):
		p5_sum += int(i)**5
	return p5_sum

ans = [i for i in xrange(2, 1000000,1) if i == int(str(p5_sum(i))) ]
print sum(ans)
#solution 2
'''print sum(i for i in xrange(2,1000000) if sum([int(n)**5 for n in str(i)]) == i)'''
