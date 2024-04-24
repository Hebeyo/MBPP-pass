'''Write a function to substract the contents of one tuple with corresponding index of other tuple.
'''
def substract_elements(test_tup1, test_tup2):
  res = []
  for i in range(len(test_tup1)):
    res.append(test_tup1[i] - test_tup2[i])
  return tuple(res)
'''
Standard answer: 
def substract_elements(test_tup1, test_tup2):
  res = tuple(map(lambda i, j: i - j, test_tup1, test_tup2))
  return (res) 
'''
assert substract_elements((10, 4, 5), (2, 5, 18)) == (8, -1, -13)
assert substract_elements((11, 2, 3), (24, 45 ,16)) == (-13, -43, -13)
assert substract_elements((7, 18, 9), (10, 11, 12)) == (-3, 7, -3)
