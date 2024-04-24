'''Write a python function to find the perimeter of a cylinder.
'''
def perimeter(diameter,height):
    return 2*(diameter+height)
'''
Standard answer: 
def perimeter(diameter,height) : 
    return 2*(diameter+height)  
'''
assert perimeter(2,4) == 12
assert perimeter(1,2) == 6
assert perimeter(3,1) == 8
