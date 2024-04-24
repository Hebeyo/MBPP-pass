'''Write a python function to find smallest power of 2 greater than or equal to n.
'''
def next_Power_Of_2(n):
    count = 0
    if (n and not(n & (n - 1))):
        return n
    while( n != 0):
        n >>= 1
        count += 1
    return 1 << count
'''
Standard answer: 
def next_Power_Of_2(n): 
    count = 0; 
    if (n and not(n & (n - 1))): 
        return n   
    while( n != 0): 
        n >>= 1
        count += 1
    return 1 << count; 
'''
assert next_Power_Of_2(0) == 1
assert next_Power_Of_2(5) == 8
assert next_Power_Of_2(17) == 32
