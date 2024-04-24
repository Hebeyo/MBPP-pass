'''Write a python function to find the last two digits in factorial of a given number.
'''
def last_Two_Digits(N): 
    if N >= 10:
        return
    fac = 1
    for i in range(1,N + 1): 
        fac = (fac * i) % 100
    return (fac)
'''
Standard answer: 
def last_Two_Digits(N): 
    if (N >= 10): 
        return
    fac = 1
    for i in range(1,N + 1): 
        fac = (fac * i) % 100
    return (fac) 
'''
assert last_Two_Digits(7) == 40
assert last_Two_Digits(5) == 20
assert last_Two_Digits(2) == 2
