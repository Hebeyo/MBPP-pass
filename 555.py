'''Write a python function to find the difference between sum of cubes of first n natural numbers and the sum of first n natural numbers.
'''
def difference(n) :  
    S = (n*(n + 1))//2;  
    res = S*(S-1);  
    return res;
'''
Standard answer: 
def difference(n) :  
    S = (n*(n + 1))//2;  
    res = S*(S-1);  
    return res;  
'''
assert difference(3) == 30
assert difference(5) == 210
assert difference(2) == 6
