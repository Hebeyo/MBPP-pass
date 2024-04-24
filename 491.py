'''Write a function to find the sum of geometric progression series.
'''
def sum_gp(a,n,r):
    total = (a * (1 - pow(r, n ))) / (1- r)
    return total
'''
Standard answer: 
import math
def sum_gp(a,n,r):
 total = (a * (1 - math.pow(r, n ))) / (1- r)
 return total
'''
assert sum_gp(1,5,2)==31
assert sum_gp(1,5,4)==341
assert sum_gp(2,6,3)==728
