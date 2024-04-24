'''Write a python function to find the cube sum of first n natural numbers.
'''
def sum_Of_Series(n):
    sum = 0
    for i in range(1, n + 1):
        sum += i * i * i
    return sum
'''
Standard answer: 
def sum_Of_Series(n): 
    sum = 0
    for i in range(1,n + 1): 
        sum += i * i*i       
    return sum
'''
assert sum_Of_Series(5) == 225
assert sum_Of_Series(2) == 9
assert sum_Of_Series(3) == 36
