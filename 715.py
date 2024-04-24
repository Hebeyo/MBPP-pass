'''Write a function to convert the given string of integers into a tuple.
'''
def str_to_tuple(test_str):
  res = tuple(map(int, test_str.split(', ')))
  return (res)
'''
Standard answer: 
def str_to_tuple(test_str):
  res = tuple(map(int, test_str.split(', ')))
  return (res) 
'''
assert str_to_tuple("1, -5, 4, 6, 7") == (1, -5, 4, 6, 7)
assert str_to_tuple("1, 2, 3, 4, 5") == (1, 2, 3, 4, 5)
assert str_to_tuple("4, 6, 9, 11, 13, 14") == (4, 6, 9, 11, 13, 14)
