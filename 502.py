'''Write a python function to find remainder of two numbers.
'''
def find(n,m):
  r = n%m
  return (r)
'''
Standard answer: 
def find(n,m):
  r = n%m
  return (r)
'''
assert find(3,3) == 0
assert find(10,3) == 1
assert find(16,5) == 1
