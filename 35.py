'''Write a function to find the n-th rectangular number.
'''
def find_rect_num(n):
    return n*(n + 1)
'''
Standard answer: 
def find_rect_num(n):
  return n*(n + 1) 
'''
assert find_rect_num(4) == 20
assert find_rect_num(5) == 30
assert find_rect_num(6) == 42
