import itertools


def is_divisible_by(value, dividor):
	return (value % dividor == 0)


def matches_property(number):
	factors = [[2, 2], [3, 3], [4, 5], [5,7], [6, 11], [7, 13], [8, 17]]

	for factor in factors:
		n = factor[0]
		divisor = factor[1]
		sub_num = int("".join(number[n-1:n+2]))  # adjust the index for zero-based list, convert to a string - then an int

		if sub_num % divisor != 0:
			return False

	return True
		#print(f"{n} = {sub_num}")


permutations = list(itertools.permutations("1234567890"))
#permutations = [["1","4","0", "6","3","5","7","2","8","9"]]

#print(len(permutations))
#print(permutations[22])



total = 0

for number in permutations:
	if(matches_property(number)):
		num = int("".join(number))
		print(num)
		total += num

print("----")
print(total)

	