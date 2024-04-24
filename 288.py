'''Write a function to count array elements having modular inverse under given prime number p equal to itself.
'''
def modular_inverse(arr, N, P):
	current_element = 0
	for i in range(0, N):
		if ((arr[i] * arr[i]) % P == 1):
			current_element = current_element + 1
	return current_element
'''
Standard answer: 
def modular_inverse(arr, N, P):
	current_element = 0
	for i in range(0, N):
		if ((arr[i] * arr[i]) % P == 1):
			current_element = current_element + 1
	return current_element
'''
assert modular_inverse([ 1, 6, 4, 5 ], 4, 7) == 2
assert modular_inverse([1, 3, 8, 12, 12], 5, 13) == 3
assert modular_inverse([2, 3, 4, 5], 4, 6) == 1
