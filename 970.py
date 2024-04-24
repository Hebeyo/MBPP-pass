'''Write a function to find minimum of two numbers.
'''
def min_of_two( x, y ):
    if x < y:
        return x
    return y
'''
Standard answer: 
def min_of_two( x, y ):
    if x < y:
        return x
    return y
'''
assert min_of_two(10,20)==10
assert min_of_two(19,15)==15
assert min_of_two(-10,-20)==-20
