#https://projecteuler.net/problem=16
#calculate the sum of the digits of the number 2**1000

print sum(int(i)for i in str(2<<999))

'''def int2list(x,y):
	list_digit = []
	while x:
		m, x = x%10**y, x/10**y
		list_digit.insert(0,int(m))
	return list_digit
print sum(int2list(2**1000,1))'''
