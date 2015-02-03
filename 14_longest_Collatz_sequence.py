#https://projecteuler.net/problem=14
#find the starting number, under one million, produces the longest Collatz chain
#for i in xrange(2,1000000,1):
def collatz_seq(x):
	cnt = 1
	next = x
	while True:
		if next == 1:
			break
		elif next%2:
			next = 3*next + 1
		else:
			next = next / 2
		cnt += 1
	return cnt

cnt_max = 0
start_max = 0
for i in xrange(1,1000000,1):
	cnt = collatz_seq(i)
	if cnt > cnt_max:
		cnt_max = cnt
		start_max = i
		print cnt_max, start_max
print 'cnt_max = {}, starter_max = {}'.format(cnt_max, start_max)
