'''Write a function to find the longest subsequence such that the difference between adjacents is one for the given array.
'''
def longest_subseq_with_diff_one(arr, n):
    dp = [1 for i in range(n)]
    for i in range(n):
        for j in range(i):
            if ((arr[i] == arr[j]+1) or (arr[i] == arr[j]-1)):
                dp[i] = max(dp[i], dp[j]+1)
    result = 1
    for i in range(n):
        if (result < dp[i]):
            result = dp[i]
    return result
'''
Standard answer: 
def longest_subseq_with_diff_one(arr, n): 
	dp = [1 for i in range(n)] 
	for i in range(n): 
		for j in range(i): 
			if ((arr[i] == arr[j]+1) or (arr[i] == arr[j]-1)): 
				dp[i] = max(dp[i], dp[j]+1) 
	result = 1
	for i in range(n): 
		if (result < dp[i]): 
			result = dp[i] 
	return result
'''
assert longest_subseq_with_diff_one([1, 2, 3, 4, 5, 3, 2], 7) == 6
assert longest_subseq_with_diff_one([10, 9, 4, 5, 4, 8, 6], 7) == 3
assert longest_subseq_with_diff_one([1, 2, 3, 2, 3, 7, 2, 1], 8) == 7
