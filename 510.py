'''Write a function to find the number of subsequences having product smaller than k for the given non negative array.
'''
def no_of_subsequences(arr, k):
    n = len(arr)
    dp = [[0 for i in range(n + 1)] 
        for j in range(k + 1)]
    for i in range(1, k + 1):
        for j in range(1, n + 1):
            dp[i][j] = dp[i][j - 1]
            if arr[j - 1] <= i and arr[j - 1] > 0:
                dp[i][j] += dp[i // arr[j - 1]][j - 1] + 1
    return dp[k][n]
'''
Standard answer: 
def no_of_subsequences(arr, k): 
	n = len(arr) 
	dp = [[0 for i in range(n + 1)] 
			for j in range(k + 1)] 
	for i in range(1, k + 1): 
		for j in range(1, n + 1): 
			dp[i][j] = dp[i][j - 1] 
			if arr[j - 1] <= i and arr[j - 1] > 0: 
				dp[i][j] += dp[i // arr[j - 1]][j - 1] + 1
	return dp[k][n]
'''
assert no_of_subsequences([1,2,3,4], 10) == 11
assert no_of_subsequences([4,8,7,2], 50) == 9
assert no_of_subsequences([5,6,7,8], 15) == 4
