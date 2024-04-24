'''Write a function to find the length of the shortest string that has both str1 and str2 as subsequences.
'''
def super_seq(X, Y, m, n):
	if (not m):
		return n
	if (not n):
		return m
	if (X[m - 1] == Y[n - 1]):
		return 1 + super_seq(X, Y, m - 1, n - 1)
	return 1 + min(super_seq(X, Y, m - 1, n),	super_seq(X, Y, m, n - 1))
'''
Standard answer: 
def super_seq(X, Y, m, n):
	if (not m):
		return n
	if (not n):
		return m
	if (X[m - 1] == Y[n - 1]):
		return 1 + super_seq(X, Y, m - 1, n - 1)
	return 1 + min(super_seq(X, Y, m - 1, n),	super_seq(X, Y, m, n - 1))
'''
assert super_seq("AGGTAB", "GXTXAYB", 6, 7) == 9
assert super_seq("feek", "eke", 4, 3) == 5
assert super_seq("PARRT", "RTA", 5, 3) == 6
