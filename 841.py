'''Write a function to count the number of inversions in the given array.
'''
def get_inv_count(arr, n):
    inv_count = 0
    for i in range(n):
        for j in range(i+1, n):
            if (arr[i] > arr[j]):
                inv_count += 1
    return inv_count
'''
Standard answer: 
def get_inv_count(arr, n): 
	inv_count = 0
	for i in range(n): 
		for j in range(i + 1, n): 
			if (arr[i] > arr[j]): 
				inv_count += 1
	return inv_count 
'''
assert get_inv_count([1, 20, 6, 4, 5], 5) == 5
assert get_inv_count([8, 4, 2, 1], 4) == 6
assert get_inv_count([3, 1, 2], 3) == 2
