#https://projecteuler.net/problem=5
from math import sqrt
def is_prime(x):
	is_prime = True
	for i in range(2,int(round(sqrt(x)+1)),1):
		if (x % i ==0):
			is_prime = False
			break
	if is_prime:
		#print x,"is a prime."
		return True
	else:
		#print x, "is not a prime."
		return False
def prim_in(x):
	return [2]+[i for i in range(3,x,2) if is_prime(i)]

#prime_list =[2]+[i for i in range(3,int(sqrt(300000000)+4),2) if is_prime(i)]

def prime_factors(x):
	factors = []
	prime_list = prim_in(int(sqrt(x)+1))
	if is_prime(x):
		#print "Prime factors cannot be found as {} itself is a prime.".format(x)
		factors.append(x)
		return factors
	status = 'undone'
	while status == "undone":
		for i in prime_list:		
			if is_prime(x):
				factors.append(x)
				status = 'done'
				break
			if (x%i == 0):
				factors.append(i)
				x /= i
				break
	return factors
def lowest_com_multiple(x,y):
	list1, list2 = prime_factors(x), prime_factors(y)
	list_inters = []
	list_joint = list1+list2
	for i in list1:
		if i in list2:
			list_inters.append(i)
			list2.remove(i)
	while len(list_inters):
			list_joint.remove(list_inters[0])
			list_inters.pop(0)
#	print "joint = {},inters={}".format(list_joint,list_inters)
#	print list_joint
#	print "lowest common muliple of {} and {} is {}".format(x,y,reduce(lambda x,y:x*y,list_joint))
#	print reduce(lambda x,y:x*y,list_joint)
	return reduce(lambda x,y:x*y,list_joint)
lowest_com_multiple(6,60)
print reduce(lowest_com_multiple,list(range(2,21,1)))
