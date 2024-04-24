'''Write a function to find the largest triangle that can be inscribed in an ellipse.
'''
def largest_triangle(a, b):
    if (a < 0 or b < 0):
        return -1
    area = (3 * 3 ** 0.5 * a ** 2) / (4 * b)
    return area
'''
Standard answer: 
import math
def largest_triangle(a,b): 
    if (a < 0 or b < 0): 
        return -1 
    area = (3 * math.sqrt(3) * pow(a, 2)) / (4 * b);  
    return area 
'''
assert largest_triangle(4,2)==10.392304845413264
assert largest_triangle(5,7)==4.639421805988064
assert largest_triangle(9,1)==105.2220865598093
