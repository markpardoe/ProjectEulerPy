# https://projecteuler.net/problem=12

import math
factor_list = {1 : [1]}  # cache any found factors for a given number
max_prime = 1  # maxiumum prime number found
max_prime_list = []  # list of primes upto the max number


# Returns list of primes up to the maxValue
def getPrimes(maxValue : int):
	primeList = []
	allNumbers =  [True] * (maxValue + 1) # Flag all numbers from 1 to end as primes
	

	for number in range(2, maxValue + 1):
		if allNumbers[number] == True:
			primeList.append(number)  #flagged as ok - so probably a prime
			for multiple_of_number in range(number * 2, maxValue + 1, number):
				allNumbers[multiple_of_number] = False

	return primeList


# Gets all factors for a number
# Tries dividing by all primes (less than number)
# If divides (remainder == 0) then try and get factors of the new number
def get_factors(number):

	if (number in factor_list):
		return factor_list[number]

	print("Get Factors For: " + str(number))
	global max_prime
	global max_prime_list

	# check if we've already generated primes upto that number
	if (max_prime < number):
		max_prime_list = getPrimes(number) # get all prime numbers
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
	return unique_factors





limit = 100 # number of factors to find
triangle = 0
number = 1

for i in range(1, 1000000):
	triangle += number
	factors = get_factors(i)

	num_factors = len(factors)
	if (num_factors >= limit):
		print(str(i) + " = " + str(num_factors))




print(len(get_factors(76576500)))




#print(get_factors(28))