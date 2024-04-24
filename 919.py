'''Write a python function to multiply all items in the list.
'''
def multiply_list(items):
    tot = 1
    for x in items:
        tot *= x
    return tot
'''
Standard answer: 
def multiply_list(items):
    tot = 1
    for x in items:
        tot *= x
    return tot
'''
assert multiply_list([1,-2,3]) == -6
assert multiply_list([1,2,3,4]) == 24
assert multiply_list([3,1,2,3]) == 18
