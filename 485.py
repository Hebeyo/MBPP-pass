'''Write a function to find the largest palindromic number in the given array.
'''
def largest_palindrome(A, n):
    A.sort()
    for i in range(n-1, -1, -1):
        if str(A[i]) == str(A[i])[::-1]:
            return A[i]
    return -1
'''
Standard answer: 
def is_palindrome(n) : 
	divisor = 1
	while (n / divisor >= 10) : 
		divisor *= 10
	while (n != 0) : 
		leading = n // divisor 
		trailing = n % 10
		if (leading != trailing) : 
			return False
		n = (n % divisor) // 10
		divisor = divisor // 100
	return True
def largest_palindrome(A, n) : 
	A.sort() 
	for i in range(n - 1, -1, -1) : 
		if (is_palindrome(A[i])) : 
			return A[i] 
	return -1
'''
assert largest_palindrome([1, 232, 54545, 999991], 4) == 54545
assert largest_palindrome([1, 2, 3, 4, 5, 50], 6) == 5
assert largest_palindrome([1, 3, 7, 9, 45], 5)  == 9
