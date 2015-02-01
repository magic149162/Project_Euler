#find the sum of the digits in number as the factorial of 100
print sum(int(i)for i in str(reduce(lambda x,y:x*y,xrange(1,101,1))))