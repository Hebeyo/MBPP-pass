'''## write a function to find the minimum number of jumps to reach the end of the array for the given array of integers where each element represents the max number of steps that can be made forward from that element. > indented block > indented block
'''
def min_jumps(arr, n):
	jumps = [0 for i in range(n)]
	if (n == 0) or (arr[0] == 0):
		return float('inf')
	jumps[0] = 0
	for i in range(1, n):
		jumps[i] = float('inf')
		for j in range(i):
			if (i <= j + arr[j]) and (jumps[j] != float('inf')):
				jumps[i] = min(jumps[i], jumps[j] + 1)
				break
	return jumps[n-1]
'''
Standard answer: 
def min_jumps(arr, n):
	jumps = [0 for i in range(n)]
	if (n == 0) or (arr[0] == 0):
		return float('inf')
	jumps[0] = 0
	for i in range(1, n):
		jumps[i] = float('inf')
		for j in range(i):
			if (i <= j + arr[j]) and (jumps[j] != float('inf')):
				jumps[i] = min(jumps[i], jumps[j] + 1)
				break
	return jumps[n-1]
'''
assert min_jumps([1, 3, 6, 1, 0, 9], 6) == 3
assert min_jumps([1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9], 11) == 3
assert min_jumps([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 11) == 10
