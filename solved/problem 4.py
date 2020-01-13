

def reverse_slicing(s):
    return s[::-1]

def IsPalindrome(number):
	string = str(number)
	rev = reverse_slicing(string)
	return string == rev

maxValue = 0  # max value found so far

for x in range(999, 100, -1):
	for y in range(x, 100, -1):
		val = x * y

		if (val < maxValue):
			break

		if IsPalindrome(val) :
			maxValue = val
			print("Max = " + str(maxValue) + ", x = " + str(x) + ", y = " + str(y))


print("----")
print(maxValue)