'''Write a function to find the ration of negative numbers in an array of integers.
'''
def negative_count(nums):
    n = len(nums)
    n1 = 0
    for x in nums:
        if x < 0:
            n1 += 1
        else:
          None
    return round(n1/n,2)
'''
Standard answer: 
from array import array
def negative_count(nums):
    n = len(nums)
    n1 = 0
    for x in nums:
        if x < 0:
            n1 += 1
        else:
          None
    return round(n1/n,2)
'''
assert negative_count([0, 1, 2, -1, -5, 6, 0, -3, -2, 3, 4, 6, 8])==0.31
assert negative_count([2, 1, 2, -1, -5, 6, 4, -3, -2, 3, 4, 6, 8])==0.31
assert negative_count([2, 4, -6, -9, 11, -12, 14, -5, 17])==0.44
