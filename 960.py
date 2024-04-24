'''Write a function to solve tiling problem.
'''
def get_noOfways(n):
    if (n == 0):
        return 0;
    if (n == 1):
        return 1; 
    return get_noOfways(n - 1) + get_noOfways(n - 2);
'''
Standard answer: 
def get_noOfways(n):
    if (n == 0):
        return 0;
    if (n == 1):
        return 1; 
    return get_noOfways(n - 1) + get_noOfways(n - 2);
'''
assert get_noOfways(4)==3
assert get_noOfways(3)==2
assert get_noOfways(5)==5
