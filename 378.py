'''Write a python function to shift last element to first position in the given list.
'''
def move_first(test_list):
  test_list = test_list[-1:] + test_list[:-1]  
  return test_list
'''
Standard answer: 
def move_first(test_list):
  test_list = test_list[-1:] + test_list[:-1]  
  return test_list
'''
assert move_first([1,2,3,4]) == [4,1,2,3]
assert move_first([0,1,2,3]) == [3,0,1,2]
assert move_first([9,8,7,1]) == [1,9,8,7]
