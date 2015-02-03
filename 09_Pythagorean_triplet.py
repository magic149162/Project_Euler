#https://projecteuler.net/problem=9
#calculate the product of the Pythagorean triplet when a+b+c = 1000 .
#Given the Triangle Inequality that the sum of the lengths of any two sides must be greater than or equal to the length of the remaining side, the length of any side should never exceed 500.
#Moreover, as the average value for a , b and c is 333.33, it sets an upper limit to the shortest side and a lower limit to the longest side.
'''
for a in range(334):
	for b in range(499,333,-1):
		if 1000*(a+b) - a*b == 500000:
			print "a = {}, b = {}, c = {}".format(a,b,1000-a-b)
			print "product of abc is {}".format(a*b*(1000-a-b))'''


for a in range(334):
	for c in range(499,333,-1):
		if 1000*(a+c) - a*c -a**2 == 500000:
			print "a = {}, b = {}, c = {}".format(a,1000-a-c,c)
			print "product of abc is {}".format(a*(1000-a-c)*c)
