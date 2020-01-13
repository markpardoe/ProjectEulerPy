digit_factorials = {}

def factorial(number):
	total = 1

	if (number in digit_factorials):
		return digit_factorials[number]

	for x in range(1, number + 1):
		total = total * x

	digit_factorials[number] = total
	return total



def is_curious(number):

	sum_of_digits = 0
	for c in str(number):
#		print(c)
		f2 = factorial(int(c))
#		print(f2)
		sum_of_digits = sum_of_digits + factorial(int(c))

		if (sum_of_digits > number):
			return False;

	return sum_of_digits == number


results = []
total = 0

for i in range(3, 1000000):
	if (is_curious(i)):
		results.append(i)
		total += i 

print(results)
print(total)


