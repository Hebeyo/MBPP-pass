'''Write a python function to find the sum of fifth power of first n even natural numbers.
'''
def even_Power_Sum(n):
    sum = 0
    for i in range(1,n+1):
        j = 2*i
        sum = sum + (j*j*j*j*j)
    return sum
'''
Standard answer: 
def even_Power_Sum(n): 
    sum = 0; 
    for i in range(1,n+1): 
        j = 2*i; 
        sum = sum + (j*j*j*j*j); 
    return sum; 
'''
assert even_Power_Sum(2) == 1056
assert even_Power_Sum(3) == 8832
assert even_Power_Sum(1) == 32
