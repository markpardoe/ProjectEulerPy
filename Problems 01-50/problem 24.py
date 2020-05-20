import itertools

limit = 9
value = 1000000
values = list(range(0, limit+1))

print(values)
permutations = list(itertools.permutations(values))
#print(permutations)

print(permutations[value - 1])
print(permutations[value])
print(permutations[value + 1])