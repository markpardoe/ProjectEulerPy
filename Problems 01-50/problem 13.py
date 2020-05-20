# https://projecteuler.net/problem=13

text_file = open("C:\Code\ProjectEuler\data\problem13_data.txt", "r")
lines = text_file.readlines()


total  = 0
for line in lines:
	total += int(line)

result = str(total)
print(result[0:10])

text_file.close()
