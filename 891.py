'''Write a python function to check whether the given two numbers have same number of digits or not.
'''
def same_Length(A,B): 
    len_A = len(str(A))
    len_B = len(str(B))
    if len_A == len_B:
        return True
    return False
'''
Standard answer: 
def same_Length(A,B): 
    while (A > 0 and B > 0): 
        A = A / 10; 
        B = B / 10; 
    if (A == 0 and B == 0): 
        return True; 
    return False; 
'''
assert same_Length(12,1) == False
assert same_Length(2,2) == True
assert same_Length(10,20) == True
