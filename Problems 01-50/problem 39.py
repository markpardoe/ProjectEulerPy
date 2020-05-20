import math
def is_square(integer):
    root = math.sqrt(integer)
    if int(root + 0.5) ** 2 == integer: 
        return True, root
    else:
        return False, 0

results = {}  # dictionary containing p : NumMatches

for a in range(1, 500):
	for b in range(a, 500):
		sqr = (a*a)+ (b*b)
		
		is_sqr, c = is_square(sqr)

		if is_sqr:
			p = int(a + b + c)

			if p in results:
				results[p] = results[p] + 1
			else:
				results[p] = 1

max_count = 0
result = 0
		
for p, count in results.items():
	if count > max_count:
		result = p
		max_count = count


print(max_count)
print(result)
#print(results[120])