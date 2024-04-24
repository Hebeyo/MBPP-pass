'''Write a function to perform mathematical division operation across the given tuples.
'''
def division_elements(test_tup1, test_tup2):
  res = []
  for i in range(len(test_tup1)):
    res.append(test_tup1[i] // test_tup2[i])
  return (tuple(res))
'''
Standard answer: 
def division_elements(test_tup1, test_tup2):
  res = tuple(ele1 // ele2 for ele1, ele2 in zip(test_tup1, test_tup2))
  return (res) 
'''
assert division_elements((10, 4, 6, 9),(5, 2, 3, 3)) == (2, 2, 2, 3)
assert division_elements((12, 6, 8, 16),(6, 3, 4, 4)) == (2, 2, 2, 4)
assert division_elements((20, 14, 36, 18),(5, 7, 6, 9)) == (4, 2, 6, 2)
