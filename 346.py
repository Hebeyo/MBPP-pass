'''Write a function to find entringer number e(n, k).
'''
def zigzag(n, k): 
	if (n == 0 and k == 0): 
		return 1
	if (k == 0): 
		return 0
	return zigzag(n, k - 1) + zigzag(n - 1, n - k)
'''
Standard answer: 
def zigzag(n, k): 
	if (n == 0 and k == 0): 
		return 1
	if (k == 0): 
		return 0
	return zigzag(n, k - 1) + zigzag(n - 1, n - k)
'''
assert zigzag(4, 3) == 5
assert zigzag(4, 2) == 4
assert zigzag(3, 1) == 1
