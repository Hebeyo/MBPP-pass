'''Write a function to find the sum of arithmetic progression.
'''
def ap_sum(a,n,d):
  total = 0
  for i in range(n):
    total += a + i * d
  return total
'''
Standard answer: 
def ap_sum(a,n,d):
  total = (n * (2 * a + (n - 1) * d)) / 2
  return total
'''
assert ap_sum(1,5,2)==25
assert ap_sum(2,6,4)==72
assert ap_sum(1,4,5)==34
