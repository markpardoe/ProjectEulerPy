import numpy as np

cell_size = 20
grid_size = cell_size + 1

# 2D array of points around cells.  Size is (grid_size + 1) x (grid_size + 1)  

grid = np.zeros((grid_size, grid_size))

grid[0,0] = 1
print(grid)

for x in range(0, grid_size):
	for y in range(0, grid_size):
		if (x == 0 and y == 0):
			grid[x, y] = 1
			continue

		print(f"Zero value = {grid[0,0]}")
		# get value of cell-junction to left
		if x == 0:  # at edge
			left_value = 0
		else:			
			left_value = grid[x-1, y]
			#print(f"({x},{y}) Left = {left_value}")

		# get value from above
		if y == 0:  # top row
			above_value = 0
		else:
			above_value = grid[x, (y-1)]

			#print(f"({x},{y}) Above = {above_value}")

		grid[x,y] = above_value + left_value

print(grid)
print(grid[cell_size, cell_size])
