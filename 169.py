'''Write a function to calculate the nth pell number.
'''
def get_pell(n):
    if n <= 2:
        return n
    a = 1
    b = 2
    for i in range(3, n+1):
        c = 2 * b + a
        a = b
        b = c
    return b
'''
Standard answer: 
def get_pell(n): 
	if (n <= 2): 
		return n 
	a = 1
	b = 2
	for i in range(3, n+1): 
		c = 2 * b + a 
		a = b 
		b = c 
	return b 
'''
assert get_pell(4) == 12
assert get_pell(7) == 169
assert get_pell(8) == 408
