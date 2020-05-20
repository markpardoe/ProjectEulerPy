# https://projecteuler.net/problem=18

text_file = open("C:\Code\ProjectEuler\data\problem67_data.txt", "r")
lines = text_file.readlines()
text_file.close()

# read in data file and convert each line to array of integers
all_lines = []
for line in lines:
	all_lines.append(list(map(int,line.split(" "))))

all_lines.reverse()  # reverese array so that last line is first

# iterate through all lines - start at 2nd from bottom  (technically top as we've reveresd the list)
for row in range(1, len(all_lines)):
	line = all_lines[row]

	for column in range(0, len(line)):
		# get values of 2 rows below
		val1 = all_lines[row-1][column]
		val2 = all_lines[row-1][column + 1]

		if val1 > val2:
			maxVal = val1
		else:
			maxVal = val2

		all_lines[row][column] = all_lines[row][column] + maxVal  # update with the maximum value (From below)


print(all_lines)
print(all_lines[len(all_lines)-1][0])