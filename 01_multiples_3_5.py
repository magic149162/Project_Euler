#https://projecteuler.net/problem=1
#Calculate the sum of all positive multipliers of 3 or 5 bellow 1000#
print sum(i for i in xrange(1000) if not(i%3 and i%5))
#Calculate the number of positive integers not the multipliers of 3,4 or 7 below 100 #
print len([i for i in xrange(100) if (i%3 and i%4 and i%7)]) 
