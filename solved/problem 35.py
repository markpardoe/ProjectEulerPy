prime_list = set()

# Returns list of primes up to the maxValue
def getPrimes(maxValue):
	primeList = set()
	allNumbers =  [True] * (maxValue + 1) # Flag all numbers from 1 to end as primes
	

	for number in range(2, maxValue + 1):
		if allNumbers[number] == True:
			primeList.add(number)  #flagged as ok - so probably a prime
			for multiple_of_number in range(number * 2, maxValue + 1, number):
				allNumbers[multiple_of_number] = False

	return primeList


def is_prime(digit_list):
	s1 = "".join(digit_list)
	value = int(s1)
	return value in prime_list

def get_rotations(number):
	results = []

	value = []
	value = list(str(number))
	for index in range(0, len(value)):
		results.append(value)

		new_value = []
		new_value.append(value[-1])  # get the last value
		new_value.extend(value[:-1]) # append all except the last value
		value = new_value


	return results


def is_circular_prime(number):
	rotations = get_rotations(number)  # get all permuations
#	print(rotations)

	for value in rotations:
		perm_value = int("".join(value))  # convert back to a string - then an int
	#	print(perm_value)
		if (perm_value not in prime_list):
		#print(f"{perm_value} is not prime!")
			return False

	return True


limit = 1000000
prime_list = getPrimes(limit*10)  # pre-calculate all primes for lookup

results = []
for prime in prime_list:
	#print(prime)
	if (prime > limit):
		continue

	if (is_circular_prime(prime)):
		results.append(prime)


print(results)
print(len(results))