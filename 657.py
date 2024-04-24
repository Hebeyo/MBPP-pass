'''Write a python function to find the first digit in factorial of a given number.
'''
def first_Digit(n) : 
    fact = 1
    for i in range(2,n + 1) : 
        fact = fact * i 
        while (fact % 10 == 0) :  
            fact = int(fact / 10) 
    while (fact >= 10) : 
        fact = int(fact / 10) 
    return fact
'''
Standard answer: 
import math 
def first_Digit(n) : 
    fact = 1
    for i in range(2,n + 1) : 
        fact = fact * i 
        while (fact % 10 == 0) :  
            fact = int(fact / 10) 
    while (fact >= 10) : 
        fact = int(fact / 10) 
    return math.floor(fact) 
'''
assert first_Digit(5) == 1
assert first_Digit(10) == 3
assert first_Digit(7) == 5
