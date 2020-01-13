limit = 20
max_reoccuring = 0


def recurring_cycle_length(number):
	str_number = str(number)
	half_length = int(len(str) / 2)

	for index in range(0, half_length):
		for c in range(1, int(len(str_number)/2):






for x in range(2, limit+1):
	
	decimal = str(1/x)[2:]

	# if the total decimal part is less than the re-occuring - no point even lookin
	if (len(decimal) < max_reoccuring):
		continue


	print(str(x) + " = " + str(decimal))


