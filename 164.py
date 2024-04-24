'''Write a python function to check whether the sum of divisors are same or not.
'''
def areEquivalent(num1,num2):
  def divSum(n): 
    sum = 1; 
    i = 2; 
    while(i * i <= n): 
        if (n % i == 0): 
            sum = (sum + i +n // i); 
        i += 1; 
    return sum; 
  return divSum(num1) == divSum(num2);
'''
Standard answer: 
import math 
def divSum(n): 
    sum = 1; 
    i = 2; 
    while(i * i <= n): 
        if (n % i == 0): 
            sum = (sum + i +math.floor(n / i)); 
        i += 1; 
    return sum; 
def areEquivalent(num1,num2): 
    return divSum(num1) == divSum(num2); 
'''
assert areEquivalent(36,57) == False
assert areEquivalent(2,4) == False
assert areEquivalent(23,47) == True
