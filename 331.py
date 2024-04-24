'''Write a python function to count unset bits of a given number.
'''
def count_unset_bits(n): 
    count = 0
    x = 1
    while(x < n + 1): 
        if ((x & n) == 0): 
            count += 1
        x = x << 1
    return count
'''
Standard answer: 
def count_unset_bits(n): 
    count = 0
    x = 1
    while(x < n + 1): 
        if ((x & n) == 0): 
            count += 1
        x = x << 1
    return count  
'''
assert count_unset_bits(2) == 1
assert count_unset_bits(4) == 2
assert count_unset_bits(6) == 1
