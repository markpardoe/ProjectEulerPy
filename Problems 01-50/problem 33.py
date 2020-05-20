def is_curious (a, b):
	a_str = str(a)
	b_str = str(b)


	if (len(a_str) != 2):
		raise Exception("invalid a")

	if (len(b_str) != 2):
		raise Exception("invalid b")

	if (a_str[1] == "0" or b_str[1] == "0"):  # trivial example (or not matching)
		return False




	if (a_str[0] == b_str[0]):
		return (a/b == int(a_str[1]) / int(b_str[1]))

	elif (a_str[0] == b_str[1]):
		return (a/b == int(a_str[1]) / int(b_str[0]))

	elif (a_str[1] == b_str[0]):
		print(f"{a} - {b}")
		if (a == 49 and b == 98):
			print(f"a/b = {a/b}")
			print(f"{a_str[0]} / {b_str[1]}  ={int(a_str[0]) / int(b_str[1])}")

		return (a/b == int(a_str[0]) / int(b_str[1]))

	elif (a_str[1] == b_str[1]):
		return (a/b == int(a_str[0]) / int(b_str[0]))

	else:
		return False



total_top = 1
toal_bottom = 1
results = []

for bottom in range(10, 100):
	for top in range(10, bottom):
		if is_curious(top, bottom):
			results.append([top, bottom])
			total_top = total_top * top
			toal_bottom = toal_bottom * bottom

print(results)

print(f"{total_top} / {toal_bottom}")

