
def is_pandigital(value):
	str_value = str(value)

	if len(str(value)) != 9:
		return False

	# convert to a character set.  Removes duplicate values
	value_set = set(str(value))

	# should be 9 unique values - and no zeros
	if (len(value_set) != 9 or "0" in value_set):
		return False
	else:
		return True

largest = 0
done = False 
for i in range(1 , 9999 ):
#for i in range(190, 195):
	#print(i)
	concat_string = str(i) 
	print(i)

	for n in range(2, 1000000):
		concat_string = concat_string + str(i*n)
		print(f"{n} = {concat_string}")
		if len(concat_string )> 9:
			break

		elif len(concat_string) == 9:
			if is_pandigital(concat_string):
				if (int(concat_string) > largest):
					largest = int(concat_string)
					print(f"i = {i}, n= {n}")



print(largest)