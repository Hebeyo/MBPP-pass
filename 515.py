'''Write a function to check if there is a subset with sum divisible by m.
'''
def modular_sum(arr, n, m):
    if (n > m):
        return True
    DP = [False for i in range(m)]
    for i in range(n):
        if (DP[0]):
            return True
        temp = [False for i in range(m)]
        for j in range(m):
            if (DP[j] == True):
                if (DP[(j + arr[i]) % m] == False):
                    temp[(j + arr[i]) % m] = True
        for j in range(m):
            if (temp[j]):
                DP[j] = True
        DP[arr[i] % m] = True
    return DP[0]
'''
Standard answer: 
def modular_sum(arr, n, m): 
	if (n > m): 
		return True
	DP = [False for i in range(m)] 
	for i in range(n): 
		if (DP[0]): 
			return True
		temp = [False for i in range(m)] 
		for j in range(m): 
			if (DP[j] == True): 
				if (DP[(j + arr[i]) % m] == False): 
					temp[(j + arr[i]) % m] = True
		for j in range(m): 
			if (temp[j]): 
				DP[j] = True
		DP[arr[i] % m] = True
	return DP[0]
'''
assert modular_sum([3, 1, 7, 5], 4, 6) == True
assert modular_sum([1, 7], 2, 5) == False
assert modular_sum([1, 6], 2, 5) == False
