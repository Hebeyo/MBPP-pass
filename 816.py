'''Write a function to clear the values of the given tuples.
'''
def clear_tuple(test_tup):
  test_tup = ()
  return (test_tup)
'''
Standard answer: 
def clear_tuple(test_tup):
  temp = list(test_tup)
  temp.clear()
  test_tup = tuple(temp)
  return (test_tup) 
'''
assert clear_tuple((1, 5, 3, 6, 8)) == ()
assert clear_tuple((2, 1, 4 ,5 ,6)) == ()
assert clear_tuple((3, 2, 5, 6, 8)) == ()
