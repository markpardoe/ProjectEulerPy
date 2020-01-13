

def is_pandigital(value):
	str_value = str(value)
	len_str = len(str_value)

	for i in range(1, len_str+1):
		if  str(i) not in str_value:
			return False

	return True

# Returns set of primes up to the maxValue
def getPrimes(maxValue):
	primeList = set()
	allNumbers =  [True] * (maxValue + 1) # Flag all numbers from 1 to end as primes
	

	for number in range(2, maxValue + 1):
		if allNumbers[number] == True:
			primeList.add(number)  #flagged as ok - so probably a prime
			for multiple_of_number in range(number * 2, maxValue + 1, number):
				allNumbers[multiple_of_number] = False

	return primeList


prime_list = list(getPrimes(987654321))
print(len(prime_list))
prime_list.sort(reverse = True)

for prime in prime_list:
	if (is_pandigital(prime)):
		print(prime)
		break

print(prime_list)