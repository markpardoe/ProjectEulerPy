import numpy as np

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



limit = 10000

checked = set()
all_primes = get_prime_set(limit)

#print(checked)

for prime in all_primes:
	checked.add(prime)

	for i in range(1, limit):
		value = prime + (2* (i*i))
		checked.add(value)

print(len(checked))

for num in range(3, limit, 2):
	if num not in checked:
		print(num)
		break