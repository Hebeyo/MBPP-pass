'''Write a function to find the count of all binary sequences of length 2n such that sum of first n bits is same as sum of last n bits.
'''
def count_binary_seq(n):
    nCr = 1
    res = 1
    for r in range(1, n + 1):
        nCr = (nCr * (n + 1 - r)) / r
        res += nCr * nCr
    return res
'''
Standard answer: 
def count_binary_seq(n): 
	nCr = 1
	res = 1
	for r in range(1, n + 1): 
		nCr = (nCr * (n + 1 - r)) / r 
		res += nCr * nCr 
	return res 
'''
assert count_binary_seq(1) == 2.0
assert count_binary_seq(2) == 6.0
assert count_binary_seq(3) == 20.0
