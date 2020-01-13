#Generator function for triangular numbers
def get_triangular_numbers():
	n = 1
	while True:
		yield int((n * (n+1)) / 2)
		n += 1  # increment step


#Generator function for triangular numbers
def get_pentagonal_numbers():
	n = 1
	while True:
		yield  int((n* ((3*n) - 1))/2)  #n(3n−1)/2	
		n += 1  # increment step

#Generator function for triangular numbers
def get_hexagonal_numbers():
	n = 1
	while True:
		#Hn=n(2n−1)
		yield int(((2 * n) - 1) * n)
	#	yield int((n * (n+1)) / 2)
		n += 1  # increment step



all_triag = set()
all_pent = set()


max_triag = 0
max_pent = 0

trig_generator = get_triangular_numbers()
pent_generator = get_pentagonal_numbers()

for hex in get_hexagonal_numbers():
	if hex <= 40755:
		continue


	
	#print(hex)
	while hex > max_triag:
		max_triag = next(trig_generator)	
		all_triag.add(max_triag)


	while hex > max_pent:
		max_pent = next(pent_generator)
		all_pent.add(max_pent)

	if (hex in all_pent and hex in all_triag):
		print(hex)
		break

print("Done")
