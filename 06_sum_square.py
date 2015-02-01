#the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum
dif=0
for n in range(1,101):
	m=list(range(1,101))
	m.remove(n)
	dif = dif+n*reduce(lambda x,y:x+y,m)
print dif
