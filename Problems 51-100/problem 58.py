# https://projecteuler.net/problem=58

# Returns set of primes up to the maxValue
def get_prime_set(maxValue):
	primeList = set()
	allNumbers =  [True] * (maxValue + 1) # Flag all numbers from 1 to end as primes
	

	for number in range(2, maxValue + 1):
		if allNumbers[number] == True:
			primeList.add(number)  #flagged as ok - so probably a prime
			for multiple_of_number in range(number * 2, maxValue + 1, number):
				allNumbers[multiple_of_number] = False

	return primeList


def get_diag_values(side_length):
	sqr_size = side_length ** 2
	digits_per_size = side_length - 1
	return [sqr_size, sqr_size - digits_per_size, sqr_size - (digits_per_size * 2), sqr_size - (digits_per_size * 3)]

all_primes = get_prime_set(1000000000)



all_diags = []
prime_count = 0

for n in range(3, 300000, 2):
	new_diags = get_diag_values(n)
	all_diags.extend(new_diags)

	for diag in new_diags:
		if diag in all_primes:
			prime_count += 1

	print(f"{n}: Diags: {len(all_diags)}.  Primes: {prime_count}. Ration = {prime_count / len(all_diags)}")

	if (prime_count / len(all_diags)) < 0.1:
		break



#print(get_diag_values(7))
