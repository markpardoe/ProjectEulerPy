# https://projecteuler.net/problem=16

power = 1000

x = (2)**power

x_string = str(x)
total = 0

for c in x_string:
	total += int(c)

print(total)
