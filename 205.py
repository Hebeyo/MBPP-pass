'''Write a function to find the inversions of tuple elements in the given tuple list.
'''
def inversion_elements(test_tup):
  res = tuple(list(map(lambda x: ~x, list(test_tup))))
  return (res)
'''
Standard answer: 
def inversion_elements(test_tup):
  res = tuple(list(map(lambda x: ~x, list(test_tup))))
  return (res) 
'''
assert inversion_elements((7, 8, 9, 1, 10, 7)) == (-8, -9, -10, -2, -11, -8)
assert inversion_elements((2, 4, 5, 6, 1, 7)) == (-3, -5, -6, -7, -2, -8)
assert inversion_elements((8, 9, 11, 14, 12, 13)) == (-9, -10, -12, -15, -13, -14)
