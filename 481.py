'''Write a function to determine if there is a subset of the given set with sum equal to the given sum.
'''
def is_subset_sum(set, n, sum):
	if (sum == 0):
		return True
	if (n == 0):
		return False
	if (set[n - 1] > sum):
		return is_subset_sum(set, n - 1, sum)
	return is_subset_sum(set, n-1, sum) or is_subset_sum(set, n-1, sum-set[n-1])
'''
Standard answer: 
def is_subset_sum(set, n, sum):
	if (sum == 0):
		return True
	if (n == 0):
		return False
	if (set[n - 1] > sum):
		return is_subset_sum(set, n - 1, sum)
	return is_subset_sum(set, n-1, sum) or is_subset_sum(set, n-1, sum-set[n-1])
'''
assert is_subset_sum([3, 34, 4, 12, 5, 2], 6, 9) == True
assert is_subset_sum([3, 34, 4, 12, 5, 2], 6, 30) == False
assert is_subset_sum([3, 34, 4, 12, 5, 2], 6, 15) == True
