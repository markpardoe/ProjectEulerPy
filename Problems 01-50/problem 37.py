

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


def is_truncatable_prime(number, prime_list):
	str_prime = str(number)  # we already know its a prime as we're only checking them

	for i in range(1, len(str_prime)):
		right = int(str_prime[i:])	

		left = int(str_prime[0:0-i])

		if (right not in prime_list) or (left not in prime_list):
			return False

	return True
		


prime_list = getPrimes(1000000)
print(is_truncatable_prime(3797, prime_list))


count = 0
total = 0
results = []

for prime in prime_list:
	if (prime <=7):
		continue
		
	if (is_truncatable_prime(prime, prime_list)):
		count += 1
		total += prime
		results.append(prime)

		if (count >= 11):
			break


print(results)
print(total)