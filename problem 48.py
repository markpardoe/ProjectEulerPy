total = 0

limit = 1000


for i in range(1, limit + 1):
	total = total + (i**i)


print(str(total)[-10:])