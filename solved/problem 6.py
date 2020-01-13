
maxValue = 100

square_total = 0
sum_total = 0

for i in range(1, maxValue+1):
	sum_total += i
	square_total += (i*i)


sum_total = sum_total * sum_total
print(sum_total)
print(square_total)

result = sum_total - square_total
print(result)


