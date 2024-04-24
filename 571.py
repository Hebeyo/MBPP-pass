'''Write a function to find maximum possible sum of disjoint pairs for the given array of integers and a number k.
'''
def max_sum_pair_diff_lessthan_K(arr, N, K):
    arr.sort()
    dp = [0] * N
    dp[0] = 0
    for i in range(1, N):
        dp[i] = dp[i-1]
        if (arr[i] - arr[i-1] < K):
            if (i >= 2):
                dp[i] = max(dp[i], dp[i-2] + arr[i] + arr[i-1])
            else:
                dp[i] = max(dp[i], arr[i] + arr[i-1])
    return dp[N - 1]
'''
Standard answer: 
def max_sum_pair_diff_lessthan_K(arr, N, K): 
	arr.sort() 
	dp = [0] * N 
	dp[0] = 0
	for i in range(1, N): 
		dp[i] = dp[i-1] 
		if (arr[i] - arr[i-1] < K): 
			if (i >= 2): 
				dp[i] = max(dp[i], dp[i-2] + arr[i] + arr[i-1]); 
			else: 
				dp[i] = max(dp[i], arr[i] + arr[i-1]); 
	return dp[N - 1]
'''
assert max_sum_pair_diff_lessthan_K([3, 5, 10, 15, 17, 12, 9], 7, 4) == 62
assert max_sum_pair_diff_lessthan_K([5, 15, 10, 300], 4, 12) == 25
assert max_sum_pair_diff_lessthan_K([1, 2, 3, 4, 5, 6], 6, 6) == 21
