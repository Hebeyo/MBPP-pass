'''Write a python function to calculate the product of all the numbers of a given tuple.
'''
def mutiple_tuple(nums):
    temp = list(nums)
    product = 1 
    for x in temp:
        product *= x
    return product
'''
Standard answer: 
def mutiple_tuple(nums):
    temp = list(nums)
    product = 1 
    for x in temp:
        product *= x
    return product
'''
assert mutiple_tuple((4, 3, 2, 2, -1, 18)) == -864
assert mutiple_tuple((1,2,3)) == 6
assert mutiple_tuple((-2,-4,-6)) == -48
