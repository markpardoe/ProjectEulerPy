# https://projecteuler.net/problem=53

factorial_cache = {}

def factorial(number):
	total = 1

	if number in factorial_cache:
		print("using cache")
		return factorial_cache[number]

	#for x in range(1, number + 1):
	for x in range(number, 0, -1):
		if x in factorial_cache:
			total = total * factorial_cache[x]
			factorial_cache[number] = total
			return total
		total = total * x

	factorial_cache[number] = total	
	return total


limit = 1000000
n_limit = 100
count = 0

for n in range(1, n_limit+1):
	for r in range(1, n+1):  # from 1 to n (inclusive)
		c =(factorial(n)) / (factorial(r)* factorial(n - r))
		if c > limit:
			count += 1


print(count)