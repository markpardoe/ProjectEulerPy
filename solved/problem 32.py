
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


limit = 987654321
max_length = 9
all_pandigitals = set()

for a in range(1, 31426):
	a_length = len(str(a))


	for b in range(a, limit):
		b_length = len(str(b))
		
		if (a_length + b_length > max_length):
			break

		product = a*b
		if (product > limit):
			break

		total = str(a) + str(b) + str(product)
		if (len(total) > max_length):
			break

		if(is_pandigital(total)):
			all_pandigitals.add(product)

print(all_pandigitals)

total = 0
for c in all_pandigitals:
	total += c

print(total)