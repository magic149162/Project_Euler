#https://projecteuler.net/problem=28
#The average value for the four numbers loacated on upper-left,upper-right,lower-left and lower-right
#equals to the number on the center left
def diag_sum(x): return int(4*(x**2 - (x-1)*1.5))
print sum(diag_sum(x)for x in xrange(3,1003,2)) + 1