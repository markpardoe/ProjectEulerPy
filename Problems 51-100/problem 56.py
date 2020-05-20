def sum_of_digits(number):

	total = 0
	for digit in str(number):
		total = total + int(digit)
	
	return total


print(sum_of_digits(1234))


max_sum = 0

for a in range(1, 100):
	for b in range (1, 100):
		digit_sum = sum_of_digits(a**b)
		if (digit_sum > max_sum):
			max_sum = digit_sum


print(max_sum)