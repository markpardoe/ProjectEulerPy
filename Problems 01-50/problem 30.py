

limit = 999999
power = 5
results = set()

for i in range (2, limit):
	str_num = str(i)
	total = 0
	for c in str_num:
		total = total + (int(c)**power)

	if total == i:
		results.add(i)

print(results)

grand_total = 0
for l in results:
	grand_total += l

print(grand_total)
