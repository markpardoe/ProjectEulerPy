

def collatz_sequence2(start_number):
	if (start_number in cached_lengths):
		return cached_lengths[start_number]

	if start_number == 1:
		return 1;


	if start_number % 2 == 0:
		#even number
		cached_lengths[start_number] = 1 + collatz_sequence2(int(start_number / 2))
	else:
		cached_lengths[start_number] = 1 + collatz_sequence2(int((3*start_number) + 1))

	#	if num in cached_list:  # already found sequence length for this number
	#		return count + cached_list[num]

		#print(num)

	return cached_lengths[start_number]


limit = 1000000

max_length = 0
final_value = 0

cached_lengths = {1 : 1}

for i in range(1, limit):
	

	l = collatz_sequence2(i)
#	print(str(i)  + " length = " + str(l))

	if l > max_length:
		final_value = i
		max_length = l

print("--------------------")
print(final_value)
print(max_length)

