# https://projecteuler.net/problem=28

total = 1  # 1 in centre at start (grd size = 1)

limit = 1001
step = 2

# For each grid size, we can just use the old size + the new points added.  
# New points =  new_points = 4(size^2) - 6(size - 1)
for grid_size in range(3, limit + step, step):
	
	new_points = (4 * (grid_size * grid_size)) - (6 * (grid_size - 1))
	total += new_points
	print(f"{grid_size} = {total}. New = {new_points}")

print(total)
