'''Write a python function to check whether the given number can be represented as difference of two squares or not.
'''
def dif_Square(n):
    for i in range(1,n):
        for j in range(1,n):
            if (i*i - j*j) == n:
                return True
    return False
'''
Standard answer: 
def dif_Square(n): 
    if (n % 4 != 2): 
        return True
    return False
'''
assert dif_Square(5) == True
assert dif_Square(10) == False
assert dif_Square(15) == True
