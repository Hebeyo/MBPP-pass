'''Write a python function to find the sum of all odd natural numbers within the range l and r.
'''
def sum_in_Range(l,r):
    sum1 = 0
    for i in range(l,r+1):
        if i%2 != 0:
            sum1 += i
    return sum1
'''
Standard answer: 
def sum_Odd(n): 
    terms = (n + 1)//2
    sum1 = terms * terms 
    return sum1  
def sum_in_Range(l,r): 
    return sum_Odd(r) - sum_Odd(l - 1)
'''
assert sum_in_Range(2,5) == 8
assert sum_in_Range(5,7) == 12
assert sum_in_Range(7,13) == 40
