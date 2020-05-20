# https://projecteuler.net/problem=27

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


limit = 1000
max_prime = 1000000
prime_list = set(getPrimes(max_prime))

# results
result_a = 0
result_b = 0
max_num_of_primes = 0


for a in range(-limit + 1, limit):
#	print(a)
	for b in range(-limit, limit+1):
		
		if (b not in prime_list):
			continue
			
		count = 0
		n = 0


		while True:
			value = (n*n) + (a*n) + b 

			# Make the cached prime list bigger!
			if (value > max_prime):
				print("Resetting primes")
				max_prime = value * 2
				prime = set(getPrimes(max_prime))

			if (value in prime_list):
			#	print(f"{n} = {value}")
				count = count + 1
				n = n + 1
			else:
				if count > max_num_of_primes:
					result_a = a
					result_b = b
					max_num_of_primes = count
					print (f"New max: a = {a}, b = {b}, num Primes = {max_num_of_primes}")
				break  # exit the loop


print(result_a*result_b)
	