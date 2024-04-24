'''Write a function to check if the given tuple contains only k elements.
'''
def check_tuples(test_tuple, K):
  res = all(ele in K for ele in test_tuple)
  return (res)
'''
Standard answer: 
def check_tuples(test_tuple, K):
  res = all(ele in K for ele in test_tuple)
  return (res) 
'''
assert check_tuples((3, 5, 6, 5, 3, 6),[3, 6, 5]) == True
assert check_tuples((4, 5, 6, 4, 6, 5),[4, 5, 6]) == True
assert check_tuples((9, 8, 7, 6, 8, 9),[9, 8, 1]) == False
