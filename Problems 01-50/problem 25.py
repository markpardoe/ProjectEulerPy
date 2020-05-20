# https://projecteuler.net/problem=25

index = 2
limit = 1000

current = 1
previous = 1


while len(str(current)) < limit:
	index += 1
	current, previous = current + previous, current

	#print (str(index) + " =  " + str(current))


print(index)
print(current)