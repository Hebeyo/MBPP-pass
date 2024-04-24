'''Write a python function to find maximum possible value for the given periodic function.
'''
def floor_Max(A,B,N):
    x = min(B - 1,N)
    return (A*x) // B
'''
Standard answer: 
def floor_Max(A,B,N):
    x = min(B - 1,N)
    return (A*x) // B
'''
assert floor_Max(11,10,9) == 9
assert floor_Max(5,7,4) == 2
assert floor_Max(2,2,1) == 1
