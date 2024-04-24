'''Write a python function to find the cube sum of first n odd natural numbers.
'''
def cube_Sum(n): 
    sum = 0   
    for i in range(0,n) : 
        sum += (2*i+1)*(2*i+1)*(2*i+1) 
    return sum
'''
Standard answer: 
def cube_Sum(n): 
    sum = 0   
    for i in range(0,n) : 
        sum += (2*i+1)*(2*i+1)*(2*i+1) 
    return sum
'''
assert cube_Sum(2) == 28
assert cube_Sum(3) == 153
assert cube_Sum(4) == 496
