class factor_finder:

	# caches for getting factors of a number
	import math
	_factor_list = {1 : set([1])}  # cache any found factors for a given number
	_prime_list = [1] # list of primes found



	# Returns list of primes up to the maxValue
	def __get_prime_set(self, maxValue):
		primeList = []
		allNumbers =  [True] * (maxValue + 1) # Flag all numbers from 1 to end as primes
		

		for number in range(2, maxValue + 1):
			if allNumbers[number] == True:
				primeList.append(number)  #flagged as ok - so probably a prime
				for multiple_of_number in range(number * 2, maxValue + 1, number):
					allNumbers[multiple_of_number] = False

		return primeList

	def getName(self):
		return "test"

	# Gets all factors for a number
	# Tries dividing by all primes (less than number)
	# If divides (remainder == 0) then try and get factors of the new number
	def get_factors(self, number):

		if (number in self._factor_list):
			return self._factor_list[number]

		# check if we've already generated primes upto that number
		if (self._prime_list[-1] < number):
			self._prime_list = self.__get_prime_set(number) # get all prime numbers

		factors = set()

		for prime in self._prime_list:
			# we only want primes upto this number
			if prime > number:
				break

			if (number % prime == 0):
				factors.add(number)
				factors.add(prime)
				new_number = int(number / prime)			
				factors.add(new_number)
				new_factors = self.get_factors(new_number)  # get factors of the new number
				factors = factors|new_factors  # mergew the 2 sets
			#	print(factors)

		self._factor_list[number] = factors
		return factors


f = factor_finder()
print(f.get_factors(25))