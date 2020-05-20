# https://projecteuler.net/problem=52

def numbers_contain_same_digits(num1, num2):
	list1 = list(str(num1))
	list2 = list(str(num2))

	list1.sort()
	list2.sort()

	return list1 == list2


limit = 6
number = 1
result_found = False 
#for number in range (1, 125880):
while not result_found:
	print(number)
	for n in range(2, (limit+1)):
		value = number * n
		
		if (not numbers_contain_same_digits(number, value)):
			break
		elif (n == limit):
			# found result
			print("Result Found:")
			print(number)
			result_found = True
			break

	number = number + 1