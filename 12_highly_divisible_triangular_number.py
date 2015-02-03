#https://projecteuler.net/problem=12
#retrieve the value of the first triangle number to have over five hundred divisors
i = 0
for x in range(1000):
	if ((x**2+x)*0.5 >=500):
		i = x
		break

cnt = 0
ans = 0
while ans == 0:
	sum = 0
	m = 1
	n = (i**2+i)*0.5
	for m in range(1,int(n**0.5)+1,1):
		#print m		
		if(n % m == 0):
			sum += 2
			#if m >= int(n**0.25 +1) and sum<= 50:
				#break

		if(sum >= 500):
			print sum
			ans = n
			#print ans
			break
	i +=1
print ans
