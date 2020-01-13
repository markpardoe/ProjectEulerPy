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

# Prime Number generator
def get_primes(maxValue):

	not_primes = {}
#	allNumbers =  [True] * (maxValue + 1) # Flag all numbers from 1 to end as primes
	
	
	for number in range(2, maxValue + 1):  #while true
		if number not in not_primes:

			# flag multples as not prime
			for multiple_of_number in range(number * 2, maxValue + 1, number):
				not_primes[multiple_of_number] = False

			yield number


def load_text_file(file_name):
	#text_file = open("C:\Code\ProjectEuler\data\problem18_data.txt", "r")
	text_file = open(file_name, "r")
	lines = text_file.readlines()
	text_file.close()
	return lines


def reverse_string(s):
    return s[::-1]


def IsPalindrome(number):
	string = str(number)
	rev = reverse_string(string)
	return string == rev

#Generator function for triangular numbers
def get_triangular_numbers():
	n = 1
	while True:
		yield int((n * (n+1)) / 2)
		n += 1  # increment step

def list_product(number_list):
# Returns product of a list of numbers
	total = 1
	for i in number_list:
		total = total * i
	return total


def is_pandigital(value):
	str_value = str(value)
	len_str = len(str_value)

	for i in range(1, len_str+1):
		if  str(i) not in str_value:
			return False

	return True


def factorial(number):
	total = 1

	for x in range(1, number + 1):
		total = total * x

	return total

# caches for getting factors of a number
import math
factor_list = {1 : [1]}  # cache any found factors for a given number
max_prime = 1  # maxiumum prime number found
max_prime_list = []  # list of primes upto the max number

# Gets all factors for a number
# Tries dividing by all primes (less than number)
# If divides (remainder == 0) then try and get factors of the new number
def get_factors(number):

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