
limit = 1000000
fraction = ""
for i in range(1, limit):
	fraction += str(i)

#print(fraction)
# print(fraction[12])



total = 1
index = 1

while index <= 1000000:
	
	total = total * int(fraction[index-1])
	print (f"{index} = {total}")
	index = index * 10


print(total)
print("done")