'''Write a function to find t-nth term of geometric series.
'''
def tn_gp(a,n,r):
    tn = a * (r ** (n - 1))
    return tn
'''
Standard answer: 
import math
def tn_gp(a,n,r):
  tn = a * (math.pow(r, n - 1))
  return tn
'''
assert tn_gp(1,5,2)==16
assert tn_gp(1,5,4)==256
assert tn_gp(2,6,3)==486
