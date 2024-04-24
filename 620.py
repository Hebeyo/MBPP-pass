'''Write a function to find the largest subset where each pair is divisible.
'''
def largest_subset(a, n):
    dp = [0 for i in range(n)]
    dp[n - 1] = 1
    for i in range(n - 2, -1, -1):
        mxm = 0
        for j in range(i + 1, n):
            if a[j] % a[i] == 0 or a[i] % a[j] == 0:
                mxm = max(mxm, dp[j])
        dp[i] = 1 + mxm
    return max(dp)
'''
Standard answer: 
def largest_subset(a, n):
	dp = [0 for i in range(n)]
	dp[n - 1] = 1; 
	for i in range(n - 2, -1, -1):
		mxm = 0;
		for j in range(i + 1, n):
			if a[j] % a[i] == 0 or a[i] % a[j] == 0:
				mxm = max(mxm, dp[j])
		dp[i] = 1 + mxm
	return max(dp)
'''
assert largest_subset([ 1, 3, 6, 13, 17, 18 ], 6) == 4
assert largest_subset([10, 5, 3, 15, 20], 5) == 3
assert largest_subset([18, 1, 3, 6, 13, 17], 6) == 4
