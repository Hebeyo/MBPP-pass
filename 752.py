'''Write a function to find the nth jacobsthal number.
'''
def jacobsthal_num(n):
  if n == 0: return 0
  if n == 1: return 1
  return jacobsthal_num(n - 1) + 2 * jacobsthal_num(n - 2)
'''
Standard answer: 
def jacobsthal_num(n): 
	dp = [0] * (n + 1) 
	dp[0] = 0
	dp[1] = 1
	for i in range(2, n+1): 
		dp[i] = dp[i - 1] + 2 * dp[i - 2] 
	return dp[n]
'''
assert jacobsthal_num(5) == 11
assert jacobsthal_num(2) == 1
assert jacobsthal_num(4) == 5
