from itertools import permutations

def isPermutation(value1, value2):
	#perms = [''.join(p) for p in permutations(str(value1))]
	#return str(value2) in perms 
	value1 = sorted(str(value1))
	value2 = sorted(str(value2))
	return value1 == value2

def get_primes(maxValue):
	not_primes = {}
#	allNumbers =  [True] * (maxValue + 1) # Flag all numbers from 1 to end as primes
	
	
	for number in range(2, maxValue + 1):  #while true
		if number not in not_primes:

			# flag multples as not prime
			for multiple_of_number in range(number * 2, maxValue + 1, number):
				not_primes[multiple_of_number] = False

			yield number



min_limit = 1000
max_limit = 9999

all_primes = []
done = False 

for prime in get_primes(max_limit):
	if (prime > min_limit) :
		all_primes.append(prime)


num = all_primes[100]



for prime in all_primes:
	if done:
		break

	#if prime <= 3330:
		#print(prime)
	#	continue


	if (prime + 3330) in all_primes and (prime + 6660) in all_primes:
		if isPermutation(prime, prime+3330) and isPermutation(prime, prime+6660):
			print(f"{prime} {prime+ 3330} {prime + 6660}")
		#		done = True
		#		break


print("Done")
