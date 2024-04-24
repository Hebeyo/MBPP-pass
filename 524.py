'''Write a function to find the sum of maximum increasing subsequence of the given array.
'''
def max_sum_increasing_subsequence(arr, n): 
  max = 0
  msis = [0 for x in range(n)] 
  for i in range(n): 
    msis[i] = arr[i] 
  for i in range(1, n): 
    for j in range(i): 
      if (arr[i] > arr[j] and msis[i] < msis[j] + arr[i]): 
        msis[i] = msis[j] + arr[i] 
  for i in range(n): 
    if max < msis[i]: 
      max = msis[i] 
  return max
'''
Standard answer: 
def max_sum_increasing_subsequence(arr, n): 
	max = 0
	msis = [0 for x in range(n)] 
	for i in range(n): 
		msis[i] = arr[i] 
	for i in range(1, n): 
		for j in range(i): 
			if (arr[i] > arr[j] and
				msis[i] < msis[j] + arr[i]): 
				msis[i] = msis[j] + arr[i] 
	for i in range(n): 
		if max < msis[i]: 
			max = msis[i] 
	return max
'''
assert max_sum_increasing_subsequence([1, 101, 2, 3, 100, 4, 5], 7) == 106
assert max_sum_increasing_subsequence([3, 4, 5, 10], 4) == 22
assert max_sum_increasing_subsequence([10, 5, 4, 3], 4) == 10
