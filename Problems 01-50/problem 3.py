
def getPrimes(maxValue):
	primeList = []
	allNumbers =  [True] * (maxValue + 1) # Flag all numbers from 1 to end as primes
	

	for number in range(2, maxValue + 1):
		if allNumbers[number] == True:
			primeList.append(number)  #flagged as ok - so probably a prime
			for multiple_of_number in range(number * 2, maxValue + 1, number):
				allNumbers[multiple_of_number] = False

	return primeList

target = 600851475143  
sqrt  = round(target **(1/2.0))  # only need to check up to the sqrt of the number

values = getPrimes(sqrt)
for i in values:
	if (target % i == 0):
		print(i)


