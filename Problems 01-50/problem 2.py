# https://projecteuler.net/problem=2

previous = 2
num = 3
total = 0

while True:
	
	if (num > 4000000):
		break
	elif (num % 2 == 0):
		
		total += num

	num = num + previous
	previous = num - previous

print(total)