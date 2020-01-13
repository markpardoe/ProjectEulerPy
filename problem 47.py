# caches for getting factors of a number
import math
factor_list = {1 : [1]}  # cache any found factors for a given number
max_prime = 1  # maxiumum prime number found
max_prime_list = []  # list of primes upto the max number

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

# Gets all factors for a number
# Tries dividing by all primes (less than number)
# If divides (remainder == 0) then try and get factors of the new number
def get_prime_factors(number):

	if (number in factor_list):
		return factor_list[number]

	global max_prime
	global max_prime_list

	# check if we've already generated primes upto that number
	if (max_prime < number):
		max_prime_list = get_prime_set_to_max(number) # get all prime numbers
		max_prime = number

	primes_list = max_prime_list

	factors = []

	for prime in primes_list:
		# we only want primes upto this number
		if prime > number:
			break

		if (number % prime == 0):
			factors.append(number)
			new_number = int(number / prime)			
			factors.append(new_number)
			factors.extend(get_factors(new_number))  # Get any factors of this number

	unique_factors = set(factors)
	factor_list[number] = list(unique_factors)
	return unique_factors
