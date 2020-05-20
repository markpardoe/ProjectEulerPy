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
		#print("Reusing factor" + str(number))
		return factor_list[number]

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
	factor_list[number] = list(unique_factors)
	return unique_factors


def sum_of_divisors(number):
	factors = get_factors(number)
	total = 0
	for x in factors:
		total += x

	return total - number # since the original number is in the factors

def is_abundant(number):
	return number < sum_of_divisors(number)

def is_perfec(number):
	return number == sum_of_divisors(number)

def is_deficient(number):
	return number > sum_of_divisors(number)


max_prime = 1000000
max_prime_list = getPrimes(max_prime)

limit = 28123  # 100
all_abundant = []  # list of all abundant numbers
sum_of_abundant = {}  # dictionary of all sums

for i in range(1, limit):
	if (is_abundant(i)):
		all_abundant.append(i)

print(len(all_abundant))

# calculate all sums and add to the dictionary (of all abundant numbers)
for i in range(0, len(all_abundant)):
	for j in range (i, len(all_abundant)):
		total = all_abundant[i] + all_abundant[j]
		if total > limit:
			break  # no point continuing if over max value
		sum_of_abundant[total] = True  # don't really care about the value

total = 0
for i in range(1, limit):
	if i not in sum_of_abundant:
		total += i

print(total)
#print(all_abundant)
#print(sum_of_abundant)