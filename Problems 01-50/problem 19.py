# https://projecteuler.net/problem=19

import datetime

start = datetime.datetime.strptime("01-01-1901", "%d-%m-%Y")
end = datetime.datetime.strptime("01-01-2001", "%d-%m-%Y")

date_generated = [start + datetime.timedelta(days=x) for x in range(0, (end-start).days)]

count = 0
for date in date_generated:
	#print(date.strftime("%d-%m-%Y"))
	
	if date.strftime("%d") =="01" and (date.strftime("%A") == "Sunday"):
		print(date.strftime("%d-%m-%Y"))
	#	print(date.strftime("%A"))
	#	print(date.strftime("%d"))
		count += 1

	
print(count)
