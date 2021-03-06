#https://projecteuler.net/problem=19
#Based on the information that 1 Jan 1900 was a Monday, calculate the number of  Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000).

#calculate the number of days in each month in a certain year based on whether it's a leap year
def days_in_month(x):
	if x % 100:
		if x % 4:
			days = [31,28,31,30,31,30,31,31,30,31,30,31]
		else:
			days = [31,29,31,30,31,30,31,31,30,31,30,31]
	elif x % 400 == 0:
		days = [31,29,31,30,31,30,31,31,30,31,30,31]
	else:
		days = [31,28,31,30,31,30,31,31,30,31,30,31]
	return days

#days_week = {'1':'Mon','2':'Tue','3':'Wed','4':'Thu','5':'Fri','6':'Sat','0':'Sun'}

first_in_year = 1 # 1 denotes Monday as 1 Jan 1900 was a Monday
first_in_month = 0
sun_cnt = 0
year = 1901
days = 0
while 1900 < year < 2001:
	days_month_last = days_in_month(year-1)
	days_month_this = days_in_month(year)
	days = sum(days_month_last)
	first_in_year = (days + first_in_year) % 7
	days_inc = 0
	for month in xrange(1,13,1):
		if month>1:
			days_inc = days_inc + days_month_this[month-2] 
		first_in_month = (days_inc + first_in_year) % 7
		if first_in_month == 0:
			sun_cnt +=1
		#print year,month, '1st was a ',days_week[str(first_in_month)]
	year += 1
print sun_cnt
