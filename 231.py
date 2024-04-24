'''Write a function to find the maximum sum in the given right triangle of numbers.
'''
def max_sum(tri, n):
    if n > 1:
        tri[1][1] = tri[1][1]+tri[0][0]
        tri[1][0] = tri[1][0]+tri[0][0]
    for i in range(2, n):
        tri[i][0] = tri[i][0] + tri[i-1][0]
        tri[i][i] = tri[i][i] + tri[i-1][i-1]
        for j in range(1, i):
            if tri[i][j]+tri[i-1][j-1] >= tri[i][j]+tri[i-1][j]:
                tri[i][j] = tri[i][j] + tri[i-1][j-1]
            else:
                tri[i][j] = tri[i][j]+tri[i-1][j]
    return (max(tri[n-1]))
'''
Standard answer: 
def max_sum(tri, n): 
	if n > 1: 
		tri[1][1] = tri[1][1]+tri[0][0] 
		tri[1][0] = tri[1][0]+tri[0][0] 
	for i in range(2, n): 
		tri[i][0] = tri[i][0] + tri[i-1][0] 
		tri[i][i] = tri[i][i] + tri[i-1][i-1] 
		for j in range(1, i): 
			if tri[i][j]+tri[i-1][j-1] >= tri[i][j]+tri[i-1][j]: 
				tri[i][j] = tri[i][j] + tri[i-1][j-1] 
			else: 
				tri[i][j] = tri[i][j]+tri[i-1][j] 
	return (max(tri[n-1]))
'''
assert max_sum([[1], [2,1], [3,3,2]], 3) == 6
assert max_sum([[1], [1, 2], [4, 1, 12]], 3) == 15 
assert max_sum([[2], [3,2], [13,23,12]], 3) == 28
