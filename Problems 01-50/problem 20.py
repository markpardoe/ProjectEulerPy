# https://projecteuler.net/problem=20

def factorial(number):
	total = 1

	for x in range(1, number + 1):
		total = total * x

	return total


number = 100

factorial_number = factorial(number)
print(factorial_number)

total = 0
for c in str(factorial_number):
	total = total + int(c)

print(total)