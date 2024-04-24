'''Write a python function to find the last digit in factorial of a given number.
'''
def last_Digit_Factorial(n): 
    fact = 1
    for i in range(1,n+1): 
        fact *= i
    return fact%10
'''
Standard answer: 
def last_Digit_Factorial(n): 
    if (n == 0): return 1
    elif (n <= 2): return n  
    elif (n == 3): return 6
    elif (n == 4): return 4 
    else: 
      return 0
'''
assert last_Digit_Factorial(4) == 4
assert last_Digit_Factorial(21) == 0
assert last_Digit_Factorial(30) == 0
