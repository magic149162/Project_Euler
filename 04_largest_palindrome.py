'''
def find_palin():
	cnt = 0
	ans = []
	for i in range(999999,99999,-1):
		#resolve each digit of the integer and store them into a list
		digits = []	
		digits_temp = map(lambda y:i/y,[100000,10000,1000,100,10,1])
		digits_temp.insert(0,0)
		for m in range(6):
			digits.append(digits_temp[m+1]-digits_temp[m]*10)
#		if i == 999990:
#			break
		for q in digits[:]:
			if q==0:
				digits.remove(q)
			else:
				break
		#check palindrome
		if digits == list(reversed(digits)):
			for num in range(999,99,-1):
				if (i%num == 0 and i/num<1000):
					status = 'found'
					ans.insert(0,i)
					cnt+=1					
					print i,"is the largest palindrome from the product of two 3-digit numbers, "\
					"and the two factors are",num,'and',i/num
					break
		#if status == 'found':
		#cnt represents the number of results currently found
		if cnt == 1:
			print ans
			break
find_palin()'''

def int_reversed(n):
	"""This function reverses an integer.

	It acquires the LSB ,then deletes it from the integer, and moves left in the pace of 10. It will deduce the reversed integer until the original MSB is added."""
	reversed = 0
	while n>0:
		reversed = reversed*10+n%10
		n = n/10
	return reversed
cnt = 0
for i in range(999999,9999,-1):
	if i == int_reversed(i):
		for num in range(1000,99,-1):
			if(i%num == 0 and i/num<1000):
				print i,"is the largest palindrome from the product of two 3-digit numbers, "\
				"and the two factors are",num,'and',i/num
				cnt+=1
				break
	if(cnt == 1000):
		break


