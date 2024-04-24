'''Write a python function to find whether the given number is present in the infinite sequence or not.
'''
def does_Contain_B(a,b,c):
    if a == b:
        return True
    if (b - a) * c > 0 and (b - a) % c == 0:
        return True
    return False
'''
Standard answer: 
def does_Contain_B(a,b,c): 
    if (a == b): 
        return True
    if ((b - a) * c > 0 and (b - a) % c == 0): 
        return True
    return False
'''
assert does_Contain_B(1,7,3) == True
assert does_Contain_B(1,-3,5) == False
assert does_Contain_B(3,2,5) == False
