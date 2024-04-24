'''Write a function to find the maximum product formed by multiplying numbers of an increasing subsequence of that array.
'''
def max_product(arr, n):
    mpis = [0] * (n)
    for i in range(n):
        mpis[i] = arr[i]
    for i in range(1, n):
        for j in range(i):
            if (arr[i] > arr[j] and mpis[i] < (mpis[j] * arr[i])):
                mpis[i] = mpis[j] * arr[i]
    return max(mpis)
'''
Standard answer: 
def max_product(arr, n ): 
	mpis =[0] * (n) 
	for i in range(n): 
		mpis[i] = arr[i] 
	for i in range(1, n): 
		for j in range(i): 
			if (arr[i] > arr[j] and
					mpis[i] < (mpis[j] * arr[i])): 
						mpis[i] = mpis[j] * arr[i] 
	return max(mpis)
'''
assert max_product([3, 100, 4, 5, 150, 6], 6) == 45000 
assert max_product([4, 42, 55, 68, 80], 5) == 50265600
assert max_product([10, 22, 9, 33, 21, 50, 41, 60], 8) == 21780000 
