'''Write a function to find out, if the given number is abundant.
'''
def is_abundant(n):
    fctrsum = 0
    for fctr in range(1, n):
        if n % fctr == 0:
            fctrsum += fctr
    return fctrsum > n
'''
Standard answer: 
def is_abundant(n):
    fctrsum = sum([fctr for fctr in range(1, n) if n % fctr == 0])
    return fctrsum > n
'''
assert is_abundant(12)==True
assert is_abundant(13)==False
assert is_abundant(9)==False
