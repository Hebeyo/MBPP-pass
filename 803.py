'''Write a python function to check whether the given number is a perfect square or not.
'''
def is_Perfect_Square(n) :
    if (n >= 0):
        if (n == 0 or n == 1):
            return True
        i = 1
        while (i * i <= n):
            if ((n % i == 0) and (n / i == i)):
                return True     
            i = i + 1
    return False
'''
Standard answer: 
def is_Perfect_Square(n) :
    i = 1
    while (i * i<= n):
        if ((n % i == 0) and (n / i == i)):
            return True     
        i = i + 1
    return False
'''
assert is_Perfect_Square(10) == False
assert is_Perfect_Square(36) == True
assert is_Perfect_Square(14) == False
