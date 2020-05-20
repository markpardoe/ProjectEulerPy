# https://projecteuler.net/problem=26


# Get prime numbers up to maxValue
def get_primes(maxValue):
	not_primes = {}
	primes = []

	for number in range(2, maxValue + 1):  #while true
		if number not in not_primes:

			# flag multples as not prime
			for multiple_of_number in range(number * 2, maxValue + 1, number):
				not_primes[multiple_of_number] = False

			primes.append(number)
	
	return primes


def count_primes(count):
	min = 1-count
	primes = get_primes(count-1)

	max_count = 0
	max_a = 0
	max_b = 0
	n = 0
	val = 0

	print(f"Range = {count}, min = {min}")
	for a in range(min, count):
		print(f"a = {a}")

		for b in primes:
			n = 1

			while True:
				val = (n*n)+ (a*n) + b
				# Check if new value is prime
				if (val in primes):
					n = n+1
				else:
					if n > max_count:
						print(f"a: {a}, b:{b}, Count = {n}")
						max_count = n
						max_a = a
						max_b = b
					break
	
	print(f"Max A = {max_a}, max B = {max_b}, max Count = {max_count}")
	print(f"Result = {max_a * max_b}")


count_primes(1000)