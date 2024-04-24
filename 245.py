'''Write a function to find the maximum sum of bi-tonic sub-sequence for the given array.
'''
def max_sum(arr, n):
    MSIBS = arr[:]
    for i in range(n):
        for j in range(0, i):
            if arr[i] > arr[j] and MSIBS[i] < MSIBS[j] + arr[i]:
                MSIBS[i] = MSIBS[j] + arr[i]
    MSDBS = arr[:]
    for i in range(1, n + 1):
        for j in range(1, i):
            if arr[-i] > arr[-j] and MSDBS[-i] < MSDBS[-j] + arr[-i]:
                MSDBS[-i] = MSDBS[-j] + arr[-i]
    max_sum = float("-Inf")
    for i, j, k in zip(MSIBS, MSDBS, arr):
        max_sum = max(max_sum, i + j - k)
    return max_sum
'''
Standard answer: 
def max_sum(arr, n): 
	MSIBS = arr[:] 
	for i in range(n): 
		for j in range(0, i): 
			if arr[i] > arr[j] and MSIBS[i] < MSIBS[j] + arr[i]: 
				MSIBS[i] = MSIBS[j] + arr[i] 
	MSDBS = arr[:] 
	for i in range(1, n + 1): 
		for j in range(1, i): 
			if arr[-i] > arr[-j] and MSDBS[-i] < MSDBS[-j] + arr[-i]: 
				MSDBS[-i] = MSDBS[-j] + arr[-i] 
	max_sum = float("-Inf") 
	for i, j, k in zip(MSIBS, MSDBS, arr): 
		max_sum = max(max_sum, i + j - k) 
	return max_sum
'''
assert max_sum([1, 15, 51, 45, 33, 100, 12, 18, 9], 9) == 194
assert max_sum([80, 60, 30, 40, 20, 10], 6) == 210
assert max_sum([2, 3 ,14, 16, 21, 23, 29, 30], 8) == 138
