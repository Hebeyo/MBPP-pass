'''Write a python function to print negative numbers in a list.
'''
def neg_nos(list1):
  for num in list1: 
    if num < 0: 
       return num
'''
Standard answer: 
def neg_nos(list1):
  for num in list1: 
    if num < 0: 
       return num 
'''
assert neg_nos([-1,4,5,-6]) == -1,-6
assert neg_nos([-1,-2,3,4]) == -1,-2
assert neg_nos([-7,-6,8,9]) == -7,-6
