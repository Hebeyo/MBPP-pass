'''Write a python function to find the maximum occuring divisor in an interval.
'''
def find_Divisor(x,y):  
    if (x==y): 
        return y 
    return 2
'''
Standard answer: 
def find_Divisor(x,y):  
    if (x==y): 
        return y 
    return 2
'''
assert find_Divisor(2,2) == 2
assert find_Divisor(2,5) == 2
assert find_Divisor(5,10) == 2
