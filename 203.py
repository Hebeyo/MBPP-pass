'''Write a python function to find the hamming distance between given two integers.
'''
def hamming_Distance(n1,n2) : 
    x = n1 ^ n2  
    setBits = 0
    while (x > 0) : 
        setBits += x & 1
        x >>= 1
    return setBits
'''
Standard answer: 
def hamming_Distance(n1,n2) : 
    x = n1 ^ n2  
    setBits = 0
    while (x > 0) : 
        setBits += x & 1
        x >>= 1
    return setBits  
'''
assert hamming_Distance(4,8) == 2
assert hamming_Distance(2,4) == 2
assert hamming_Distance(1,2) == 2
