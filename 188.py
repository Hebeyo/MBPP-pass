'''Write a python function to check whether the given number can be represented by product of two squares or not.
'''
def prod_Square(n):
    for i in range(2,(n) + 1):
        if (i*i < (n+1)):
            for j in range(2,n + 1):
                if ((i*i*j*j) == n):
                    return True;
    return False;
'''
Standard answer: 
def prod_Square(n):
    for i in range(2,(n) + 1):
        if (i*i < (n+1)):
            for j in range(2,n + 1):
                if ((i*i*j*j) == n):
                    return True;
    return False;
'''
assert prod_Square(25) == False
assert prod_Square(30) == False
assert prod_Square(16) == True
