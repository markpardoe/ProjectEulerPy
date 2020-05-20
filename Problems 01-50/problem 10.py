# https://projecteuler.net/problem=10

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

limit = 2000000

primes = getPrimes(limit)

total = 0
for i in primes:
	total = total + i

#print(primes)
print(total)