'''Write a python function to find the slope of a line.
'''
def slope(x1,y1,x2,y2):
    return (y2-y1)/(x2-x1)
'''
Standard answer: 
def slope(x1,y1,x2,y2): 
    return (float)(y2-y1)/(x2-x1)  
'''
assert slope(4,2,2,5) == -1.5
assert slope(2,4,4,6) == 1
assert slope(1,2,4,2) == 0
