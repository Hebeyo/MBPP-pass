'''Write a python function to count negative numbers in a list.
'''
def neg_count(list):
  neg_count= 0
  for num in list: 
    if num <= 0: 
      neg_count += 1
  return neg_count
'''
Standard answer: 
def neg_count(list):
  neg_count= 0
  for num in list: 
    if num <= 0: 
      neg_count += 1
  return neg_count 
'''
assert neg_count([-1,-2,3,-4,-5]) == 4
assert neg_count([1,2,3]) == 0
assert neg_count([1,2,-3,-10,20]) == 2
