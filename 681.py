'''Write a python function to find the smallest prime divisor of a number.
'''
def smallest_Divisor(n): 
    if (n % 2 == 0): 
        return 2; 
    i = 3;  
    while (i*i <= n): 
        if (n % i == 0): 
            return i; 
        i += 2; 
    return n;
'''
Standard answer: 
def smallest_Divisor(n): 
    if (n % 2 == 0): 
        return 2; 
    i = 3;  
    while (i*i <= n): 
        if (n % i == 0): 
            return i; 
        i += 2; 
    return n; 
'''
assert smallest_Divisor(10) == 2
assert smallest_Divisor(25) == 5
assert smallest_Divisor(31) == 31
