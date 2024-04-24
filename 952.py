'''Write a function to compute the value of ncr mod p.
'''
def nCr_mod_p(n, r, p):
    C = [0 for i in range(r + 1)]
    C[0] = 1
    for i in range(1, n + 1):
        for j in range(min(i, r), 0, -1):
            C[j] = (C[j] + C[j-1]) % p
    return C[r]
'''
Standard answer: 
def nCr_mod_p(n, r, p): 
	if (r > n- r): 
		r = n - r 
	C = [0 for i in range(r + 1)] 
	C[0] = 1 
	for i in range(1, n + 1): 
		for j in range(min(i, r), 0, -1): 
			C[j] = (C[j] + C[j-1]) % p 
	return C[r] 
'''
assert nCr_mod_p(10, 2, 13) == 6
assert nCr_mod_p(11, 3, 14) == 11
assert nCr_mod_p(18, 14, 19) == 1
