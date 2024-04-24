'''Write a function to perfom the modulo of tuple elements in the given two tuples.
'''
def tuple_modulo(test_tup1, test_tup2):
  res = []
  for i in range(len(test_tup1)):
    res.append(test_tup1[i] % test_tup2[i])
  return (tuple(res))
'''
Standard answer: 
def tuple_modulo(test_tup1, test_tup2):
  res = tuple(ele1 % ele2 for ele1, ele2 in zip(test_tup1, test_tup2)) 
  return (res) 
'''
assert tuple_modulo((10, 4, 5, 6), (5, 6, 7, 5)) == (0, 4, 5, 1)
assert tuple_modulo((11, 5, 6, 7), (6, 7, 8, 6)) == (5, 5, 6, 1)
assert tuple_modulo((12, 6, 7, 8), (7, 8, 9, 7)) == (5, 6, 7, 1)
