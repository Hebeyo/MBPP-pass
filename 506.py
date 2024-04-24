'''Write a function to calculate the permutation coefficient of given p(n, k).
'''
def permutation_coefficient(n, k):
  P = [[0 for i in range(k + 1)] 
      for j in range(n + 1)] 
  for i in range(n + 1): 
    for j in range(min(i, k) + 1): 
      if (j == 0): 
        P[i][j] = 1
      else: 
        P[i][j] = P[i - 1][j] + ( 
            j * P[i - 1][j - 1]) 
      if (j < k): 
        P[i][j + 1] = 0
  return P[n][k]
'''
Standard answer: 
def permutation_coefficient(n, k): 
	P = [[0 for i in range(k + 1)] 
			for j in range(n + 1)] 
	for i in range(n + 1): 
		for j in range(min(i, k) + 1): 
			if (j == 0): 
				P[i][j] = 1
			else: 
				P[i][j] = P[i - 1][j] + ( 
						j * P[i - 1][j - 1]) 
			if (j < k): 
				P[i][j + 1] = 0
	return P[n][k] 
'''
assert permutation_coefficient(10, 2) == 90
assert permutation_coefficient(10, 3) == 720
assert permutation_coefficient(10, 1) == 10
