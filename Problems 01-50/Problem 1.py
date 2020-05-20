# https://projecteuler.net/problem=1

total = 0
for x in range(1, 1000000000):
	if (x %3 == 0 or x %5 == 0):
		total += x
print(total)