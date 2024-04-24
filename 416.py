'''Write a function to find the maximum sum we can make by dividing number in three parts recursively and summing them up together for the given number.
'''
def breakSum(n): 
	if (n == 0 or n == 1): 
		return n
	return max(n, breakSum(int(n/2)) + breakSum(int(n/3)) + breakSum(int(n/4)))
'''
Standard answer: 
MAX = 1000000
def breakSum(n): 
	dp = [0]*(n+1) 
	dp[0] = 0
	dp[1] = 1
	for i in range(2, n+1): 
		dp[i] = max(dp[int(i/2)] + dp[int(i/3)] + dp[int(i/4)], i); 
	return dp[n]
'''
assert breakSum(12) == 13
assert breakSum(24) == 27
assert breakSum(23) == 23
