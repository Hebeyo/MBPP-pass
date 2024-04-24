'''Write a function to find the maximum length of the subsequence with difference between adjacent elements for the given array.
'''
def max_len_sub( arr, n): 
	mls=[] 
	max = 0
	for i in range(n): 
		mls.append(1) 
	for i in range(n): 
		for j in range(i): 
			if (abs(arr[i] - arr[j]) <= 1 and mls[i] < mls[j] + 1): 
				mls[i] = mls[j] + 1
	for i in range(n): 
		if (max < mls[i]): 
			max = mls[i] 
	return max
'''
Standard answer: 
def max_len_sub( arr, n): 
	mls=[] 
	max = 0
	for i in range(n): 
		mls.append(1) 
	for i in range(n): 
		for j in range(i): 
			if (abs(arr[i] - arr[j]) <= 1 and mls[i] < mls[j] + 1): 
				mls[i] = mls[j] + 1
	for i in range(n): 
		if (max < mls[i]): 
			max = mls[i] 
	return max
'''
assert max_len_sub([2, 5, 6, 3, 7, 6, 5, 8], 8) == 5
assert max_len_sub([-2, -1, 5, -1, 4, 0, 3], 7) == 4
assert max_len_sub([9, 11, 13, 15, 18], 5) == 1
