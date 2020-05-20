def reverse_slicing(s):
    return s[::-1]


def IsPalindrome(number):
	string = str(number)
	rev = reverse_slicing(string)
	return string == rev


def is_Lychrel(number):
	original_number = number
	for n in range(0,50):
		reverse =  int(reverse_slicing(str(number)))
		number = number + reverse

		if IsPalindrome(number):

			print (f"{original_number}.  gen {n+1} = {number - reverse} + {reverse}")
			return False

	return True


count = 0

for n in range(1, 10000):
	if (is_Lychrel(n)):
		count += 1

print(count)