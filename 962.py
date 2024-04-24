'''Write a python function to find the sum of all even natural numbers within the range l and r.
'''
def sum_Even(l,r): 
    return (int(r / 2) * (int(r / 2) + 1)) - (int((l - 1) / 2) * (int((l - 1) / 2) + 1))
'''
Standard answer: 
def sum_Natural(n): 
    sum = (n * (n + 1)) 
    return int(sum) 
def sum_Even(l,r): 
    return (sum_Natural(int(r / 2)) - sum_Natural(int((l - 1) / 2))) 
'''
assert sum_Even(2,5) == 6
assert sum_Even(3,8) == 18
assert sum_Even(4,6) == 10
