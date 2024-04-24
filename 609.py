'''Write a python function to find minimum possible value for the given periodic function.
'''
def floor_Min(A,B,N):
    x = max(B - 1,N)
    return (A*x) // B
'''
Standard answer: 
def floor_Min(A,B,N):
    x = max(B - 1,N)
    return (A*x) // B
'''
assert floor_Min(10,20,30) == 15
assert floor_Min(1,2,1) == 0
assert floor_Min(11,10,9) == 9
