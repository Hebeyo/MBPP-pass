'''Write a function to concatenate the given two tuples to a nested tuple.
'''
def concatenate_nested(test_tup1, test_tup2):
  res = test_tup1 + test_tup2
  return (res)
'''
Standard answer: 
def concatenate_nested(test_tup1, test_tup2):
  res = test_tup1 + test_tup2
  return (res) 
'''
assert concatenate_nested((3, 4), (5, 6)) == (3, 4, 5, 6)
assert concatenate_nested((1, 2), (3, 4)) == (1, 2, 3, 4)
assert concatenate_nested((4, 5), (6, 8)) == (4, 5, 6, 8)
