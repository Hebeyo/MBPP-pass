'''Write a function to find the length of the longest sub-sequence such that elements in the subsequences are consecutive integers.
'''
def find_longest_conseq_subseq(arr, n):
    s = set()
    ans = 0
    for ele in arr:
        s.add(ele)
    for i in range(n):
        if arr[i]-1 not in s:
            j = arr[i]
            while j in s:
                j += 1
            ans = max(ans, j-arr[i])
    return ans
'''
Standard answer: 
def find_longest_conseq_subseq(arr, n): 
	ans = 0
	count = 0
	arr.sort() 
	v = [] 
	v.append(arr[0]) 
	for i in range(1, n): 
		if (arr[i] != arr[i - 1]): 
			v.append(arr[i]) 
	for i in range(len(v)): 
		if (i > 0 and v[i] == v[i - 1] + 1): 
			count += 1
		else: 
			count = 1
		ans = max(ans, count) 
	return ans 
'''
assert find_longest_conseq_subseq([1, 2, 2, 3], 4) == 3
assert find_longest_conseq_subseq([1, 9, 3, 10, 4, 20, 2], 7) == 4
assert find_longest_conseq_subseq([36, 41, 56, 35, 44, 33, 34, 92, 43, 32, 42], 11) == 5
