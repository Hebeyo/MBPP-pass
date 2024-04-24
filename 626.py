'''Write a python function to find the largest triangle that can be inscribed in the semicircle.
'''
def triangle_area(r) :  
    if r < 0 : 
        return -1
    return r * r
'''
Standard answer: 
def triangle_area(r) :  
    if r < 0 : 
        return -1
    return r * r 
'''
assert triangle_area(0) == 0
assert triangle_area(-1) == -1
assert triangle_area(2) == 4
