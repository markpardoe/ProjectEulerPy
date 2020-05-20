# https://projecteuler.net/problem=5

initialValue = 20


def isEvenlyDivisible(num_to_check, max_divisor):
	for x in (range(1, max_divisor)):
		if num_to_check % x != 0:
			return False
	return True

# Returns list of primes up to the maxValue
def getPrimes(maxValue):
	primeList = []
	allNumbers =  [True] * (maxValue + 1) # Flag all numbers from 1 to end as primes
	

	for number in range(2, maxValue + 1):
		if allNumbers[number] == True:
			primeList.append(number)  #flagged as ok - so probably a prime
			for multiple_of_number in range(number * 2, maxValue + 1, number):
				allNumbers[multiple_of_number] = False

	return primeList

primes = getPrimes(initialValue)

multiplier = 2
total = 1

for i in primes:
	total = total * i


while(True):
	value = total * multiplier
	multiplier = multiplier + 1
	if (isEvenlyDivisible(value, initialValue)):
		print(value)
		break;

	if (value > 1000000000):
		print("Too big")
		break

print(value)