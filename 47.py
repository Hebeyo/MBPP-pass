'''Write a python function to find the last digit when factorial of a divides factorial of b.
'''
def compute_Last_Digit(A,B):
    variable = 1
    if (A == B):
        return 1
    elif ((B - A) >= 5):
        return 0
    else:
        for i in range(A + 1,B + 1):
            variable = (variable * (i % 10)) % 10
        return variable % 10
'''
Standard answer: 
def compute_Last_Digit(A,B): 
    variable = 1
    if (A == B): 
        return 1
    elif ((B - A) >= 5):  
        return 0
    else:   
        for i in range(A + 1,B + 1): 
            variable = (variable * (i % 10)) % 10
        return variable % 10
'''
assert compute_Last_Digit(2,4) == 2
assert compute_Last_Digit(6,8) == 6
assert compute_Last_Digit(1,2) == 2
assert compute_Last_Digit(3,7) == 0
assert compute_Last_Digit(20,23) == 6
assert compute_Last_Digit(1021,1024) == 4
