def generate_triangle(min_number, max_number):
	n = 1
	results = set()
	while True:
		value = int((n*(n+1)) / 2)
		n += 1
		
		if value >= min_number and value <= max_number:
			results.add(value)

		if (value > max_number):
			break
	return results

def generate_square(min_number,max_number):
	n = 1
	results = set()
	while True:
		value = int(n*n)
		n += 1
		if value >= min_number and value <= max_number:
			results.add(value)

		if (value > max_number):
			break
	return results

def generate_Pentagonal(min_number,max_number):
	n = 1
	results = set()
	while True:
		value = int((((3*n)-1)*n)/2)
		n += 1

		if value >= min_number and value <= max_number:
			results.add(value)

		if (value > max_number):
			break
	return results


def generate_hexagonal(min_number,max_number):
	n = 1
	results = set()
	while True:
		value = int(((2*n)-1)*n)
		n += 1

		if value >= min_number and value <= max_number:
			results.add(value)

		if (value > max_number):
			break
	return results

def generate_heptagonal(min_number,max_number):
	n = 1
	results = set()
	while True:
		value = int((((n*5) - 3) * n)/ 2)
		n += 1

		if value >= min_number and value <= max_number:
			results.add(value)

		if (value > max_number):
			break
	return results

def generate_octagonal(min_number,max_number):
	n = 1
	results = set()
	while True:
		value = int(((3*n)-2)*n)
		n += 1

		if value >= min_number and value <= max_number:
			results.add(value)

		if (value > max_number):
			break
	return results	


def is_cyclical_forward(number1, number2):
#	print(str(number1)[2:])

#	print(str(number2)[:2])
	return str(number1)[2:] ==  str(number2)[:2]

def find_cyclical(list_of_sets):
	checked =[False] * len(list_of_sets)
	print(checked)


max_limit = 9999
min_limit = 1000
triangles = generate_triangle(min_limit, max_limit)
squares = generate_square(min_limit, max_limit)
pentagonals = generate_Pentagonal(min_limit, max_limit)
hexagonal = generate_hexagonal(min_limit, max_limit)
heptagonal = generate_heptagonal(min_limit, max_limit)
octagonal = generate_octagonal(min_limit, max_limit)

print(triangles)

print(is_cyclical_forward(1234, 3512))

for tri in triangles:
	for pent in pentagonals:
		if is_cyclical_forward(tri, pent):
			for sqr in squares:
				if is_cyclical_forward(pent, sqr) and is_cyclical_forward(sqr, tri):
					print(f"{tri}, {pent}, {sqr}")


find_cyclical([triangles, pentagonals])
#for tri in triangles:
	#if tri < 1000 or tri > 9999:
#		break