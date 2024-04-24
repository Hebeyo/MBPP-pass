'''Write a python function to find the sum of fifth power of n natural numbers.
'''
def fifth_Power_Sum(n):
    sum = 0
    for i in range(1,n+1):
        sum = sum + (i*i*i*i*i)
    return sum
'''
Standard answer: 
def fifth_Power_Sum(n) : 
    sm = 0 
    for i in range(1,n+1) : 
        sm = sm + (i*i*i*i*i) 
    return sm 
'''
assert fifth_Power_Sum(2) == 33
assert fifth_Power_Sum(4) == 1300
assert fifth_Power_Sum(3) == 276
