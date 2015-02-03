#https://projecteuler.net/problem=26
#Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part
#run unit division operation recursively and store each remainder in a list, and the division calculation
#should not stop until current remainder occured in the list once before, which means the  calculation
#is entering another recurring cycle. The index difference between those two remainders is exactly
#the length of the cycle.

max_len = 0
rec = 0
ans_quo = []
#def rec_cy(x):

for i in xrange(2,1000):
	if (1000%i == 0):
		continue
	rema = []
	quot = []
	rem = 1
	while (rem != 0):
		rem *=10
		quo = rem / i
		rem = rem % i
		if (rem in rema):
			quo_len = len(rema[rema.index(rem):])
			if quo_len > max_len:
				max_len = quo_len
				rec = i
				#ans_quo = quot
			break
		rema.append(rem)
		#quot.append(quo)
print rec
