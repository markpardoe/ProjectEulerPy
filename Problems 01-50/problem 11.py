# https://projecteuler.net/problem=11

def load_text_file(file_name):
	#text_file = open("C:\Code\ProjectEuler\data\problem18_data.txt", "r")
	text_file = open(file_name, "r")
	lines = text_file.readlines()
	text_file.close()
	return lines


lines = load_text_file("C:\Code\ProjectEuler\data\p011_grid.txt")

grid = []
index = 0
for row in lines:
	row.rstrip()

	row = row.split()
	grid.append(list(map(int, row)))
	#print(f"{index} = {row}")


grid_size = len(grid)

print(grid_size)

largest_product = 0

for y in range(0, grid_size):  # work down columns
	for x in range(0, grid_size):  # then across rows
		
		# get product to right
		if (x <= grid_size - 4):  # check we're not hitting right-hand edge
			product = grid[y][x] * grid[y][x+1] * grid[y][x+2] * grid[y][x+3]
			if product > largest_product:
				print(f"Right: x({x}), y({y}) = {product}")
				largest_product = product
		
		# get product to right
		if (y <= grid_size - 4):  # check we're not hitting right-hand edge
			product = grid[y][x] * grid[y+1][x] * grid[y+2][x] * grid[y+3][x]
			if product > largest_product:
				print(f"Down: x({x}), y({y}) = {product}")
				largest_product = product

		# get product diag down to right
		if (y <= grid_size - 4 and x <= grid_size - 4):  # check we're not hitting right-hand edge
			product = grid[y][x] * grid[y+1][x+1] * grid[y+2][x+2] * grid[y+3][x+3]
			if product > largest_product:
				print(f"Diag: x({x}), y({y}) = {product}")
				largest_product = product

		# get product diag up to right
		if (y >= 4 and x <= grid_size - 4):  # check we're not hitting right-hand edge
			product = grid[y][x] * grid[y-1][x+1] * grid[y-2][x+2] * grid[y-3][x+3]
			if product > largest_product:
				print(f"Diag up: x({x}), y({y}) = {product}")
				largest_product = product
print(largest_product)