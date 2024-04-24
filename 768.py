'''Write a python function to check for odd parity of a given number.
'''
def check_Odd_Parity(x):
    parity = 0
    while (x != 0):
        x = x & (x - 1)
        parity += 1
    if (parity % 2 == 1):
        return True
    else:
        return False
'''
Standard answer: 
def check_Odd_Parity(x): 
    parity = 0
    while (x != 0): 
        x = x & (x - 1) 
        parity += 1
    if (parity % 2 == 1): 
        return True
    else: 
        return False
'''
assert check_Odd_Parity(13) == True
assert check_Odd_Parity(21) == True
assert check_Odd_Parity(18) == False
