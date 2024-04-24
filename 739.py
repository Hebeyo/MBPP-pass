'''Write a python function to find the index of smallest triangular number with n digits.
'''
def find_Index(n): 
    return round((2 * 10**(n - 1))**0.5)
'''
Standard answer: 
import math 
def find_Index(n): 
    x = math.sqrt(2 * math.pow(10,(n - 1))); 
    return round(x); 
'''
assert find_Index(2) == 4
assert find_Index(3) == 14
assert find_Index(4) == 45
