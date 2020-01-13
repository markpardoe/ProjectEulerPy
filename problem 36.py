def is_palindromic(number):
	num = str(number)
	num_length = len(num)
	half_length = int(num_length/2)

	for i in range(0, half_length):
	#	print(f"i = {i}. {num[i]} == {num[-1-i]}" )
		if num[i] != num[-1-i]:
			return False

	return True


total = 0
limit = 1000000

for num in range(1, limit):
	if is_palindromic(num):
		binary = bin(num)
		binary = str(binary)[2:]

		if (is_palindromic(binary)):
			print(f"{num} = {binary}")
			total = total + num 
		


print(total)

