'''Write a function to swap two numbers.
'''
def swap_numbers(a,b):
    a = a + b
    b = a - b
    a = a - b
    return (a,b)
'''
Standard answer: 
def swap_numbers(a,b):
 temp = a
 a = b
 b = temp
 return (a,b)
'''
assert swap_numbers(10,20)==(20,10)
assert swap_numbers(15,17)==(17,15)
assert swap_numbers(100,200)==(200,100)
