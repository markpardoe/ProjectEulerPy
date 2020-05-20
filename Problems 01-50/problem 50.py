# Returns set of primes up to the maxValue
def get_prime_set(maxValue):
	primeList = set()
	allNumbers =  [True] * (maxValue + 1) # Flag all numbers from 1 to end as primes
	

	for number in range(2, maxValue + 1):
		if allNumbers[number] == True:
			primeList.add(number)  #flagged as ok - so probably a prime
			for multiple_of_number in range(number * 2, maxValue + 1, number):
				allNumbers[multiple_of_number] = False

	primeList = list(primeList)
	primeList.sort()
	return primeList

limit = 1000
all_primes = get_prime_set(limit)

max_count = 0
max_prime = 0
max_total = 0
print(all_primes)

for idx, prime in enumerate(all_primes):
	
	#print(f"{idx} - {prime}" )
	count = 0
	prime_total = prime

	# stop us going above the maximum prime value (and hitting out-of-range error)
	if (idx + 1 == len(all_primes)):
		print("Ending list at last index")
		break  # end of list

	for n in range(idx + 1, len(all_primes)-2):
		count = count + 1
		next_prime = all_primes[n+1]
		prime_total += next_prime
	#	print(f"Checking Prime {prime}.  N = {n}.  Next Prime = {next_prime}.  Value = {prime_total}. Count = {count}")

		if (prime_total in all_primes):
		#	print(f"count = {count}")		
	
			if count > max_count:
				max_count = count
				max_prime = prime
				max_total = prime_total
				
print(max_prime)
print(max_count)
print(prime_total)