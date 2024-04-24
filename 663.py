'''Write a function to find the largest possible value of k such that k modulo x is y.
'''
def find_max_val(n, x, y):
    ans = -float('inf')
    for k in range(n + 1):
        if (k % x == y):
            ans = max(ans, k)
    return (ans if (ans >= 0 and ans <= n) else -1)
'''
Standard answer: 
import sys 
def find_max_val(n, x, y): 
	ans = -sys.maxsize 
	for k in range(n + 1): 
		if (k % x == y): 
			ans = max(ans, k) 
	return (ans if (ans >= 0 and
					ans <= n) else -1) 
'''
assert find_max_val(15, 10, 5) == 15
assert find_max_val(187, 10, 5) == 185
assert find_max_val(16, 11, 1) == 12
