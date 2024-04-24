'''Write a function to combine two given sorted lists using heapq module.
'''
def combine_lists(num1,num2):
  from heapq import merge
  combine_lists=list(merge(num1, num2))
  return combine_lists
'''
Standard answer: 
from heapq import merge
def combine_lists(num1,num2):
  combine_lists=list(merge(num1, num2))
  return combine_lists
'''
assert combine_lists([1, 3, 5, 7, 9, 11],[0, 2, 4, 6, 8, 10])==[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
assert combine_lists([1, 3, 5, 6, 8, 9], [2, 5, 7, 11])==[1,2,3,5,5,6,7,8,9,11]
assert combine_lists([1,3,7],[2,4,6])==[1,2,3,4,6,7]
