'''Write a function to find a path with the maximum average over all existing paths for the given square matrix of size n*n.
'''
def maxAverageOfPath(cost, N):
  dp = [[0 for i in range(N + 1)] for j in range(N + 1)]
  dp[0][0] = cost[0][0]
  for i in range(1, N):
    dp[i][0] = dp[i - 1][0] + cost[i][0]
  for j in range(1, N):
    dp[0][j] = dp[0][j - 1] + cost[0][j]
  for i in range(1, N):
    for j in range(1, N):
      dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]) + cost[i][j]
  return dp[N - 1][N - 1] / (2 * N - 1)
'''
Standard answer: 
M = 100
def maxAverageOfPath(cost, N): 
	dp = [[0 for i in range(N + 1)] for j in range(N + 1)] 
	dp[0][0] = cost[0][0] 
	for i in range(1, N): 
		dp[i][0] = dp[i - 1][0] + cost[i][0] 
	for j in range(1, N): 
		dp[0][j] = dp[0][j - 1] + cost[0][j] 
	for i in range(1, N): 
		for j in range(1, N): 
			dp[i][j] = max(dp[i - 1][j], 
						dp[i][j - 1]) + cost[i][j] 
	return dp[N - 1][N - 1] / (2 * N - 1)
'''
assert maxAverageOfPath([[1, 2, 3], [6, 5, 4], [7, 3, 9]], 3) == 5.2
assert maxAverageOfPath([[2, 3, 4], [7, 6, 5], [8, 4, 10]], 3) == 6.2
assert maxAverageOfPath([[3, 4, 5], [8, 7, 6], [9, 5, 11]], 3) == 7.2 
