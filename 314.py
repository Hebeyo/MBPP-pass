'''Write a function to find out the maximum sum such that no two chosen numbers are adjacent for the given rectangular grid of dimension 2 x n.
'''
def max_sum_rectangular_grid(grid, n) : 
	incl = max(grid[0][0], grid[1][0]) 
	excl = 0
	for i in range(1, n) : 
		excl_new = max(excl, incl) 
		incl = excl + max(grid[0][i], grid[1][i]) 
		excl = excl_new 
	return max(excl, incl)
'''
Standard answer: 
def max_sum_rectangular_grid(grid, n) : 
	incl = max(grid[0][0], grid[1][0]) 
	excl = 0
	for i in range(1, n) : 
		excl_new = max(excl, incl) 
		incl = excl + max(grid[0][i], grid[1][i]) 
		excl = excl_new 
	return max(excl, incl)
'''
assert max_sum_rectangular_grid([ [1, 4, 5], [2, 0, 0 ] ], 3) == 7
assert max_sum_rectangular_grid([ [ 1, 2, 3, 4, 5], [ 6, 7, 8, 9, 10] ], 5) == 24
assert max_sum_rectangular_grid([ [7, 9, 11, 15, 19], [21, 25, 28, 31, 32] ], 5) == 81
