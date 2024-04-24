'''Write a function to find the greatest common divisor (gcd) of two integers by using recursion.
'''
def recur_gcd(a, b):
    if a == 0:
        return b
    return recur_gcd(b % a, a)
'''
Standard answer: 
def recur_gcd(a, b):
	low = min(a, b)
	high = max(a, b)
	if low == 0:
		return high
	elif low == 1:
		return 1
	else:
		return recur_gcd(low, high%low)
'''
assert recur_gcd(12,14) == 2
assert recur_gcd(13,17) == 1
assert recur_gcd(9, 3) == 3
