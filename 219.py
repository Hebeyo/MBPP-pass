'''Write a function to extract maximum and minimum k elements in the given tuple.
'''
def extract_min_max(test_tup, K):
  res = []
  test_tup = list(test_tup)
  temp = sorted(test_tup)
  for idx, val in enumerate(temp):
    if idx < K or idx >= len(temp) - K:
      res.append(val)
  res = tuple(res)
  return (res)
'''
Standard answer: 

def extract_min_max(test_tup, K):
  res = []
  test_tup = list(test_tup)
  temp = sorted(test_tup)
  for idx, val in enumerate(temp):
    if idx < K or idx >= len(temp) - K:
      res.append(val)
  res = tuple(res)
  return (res) 
'''
assert extract_min_max((5, 20, 3, 7, 6, 8), 2) == (3, 5, 8, 20)
assert extract_min_max((4, 5, 6, 1, 2, 7), 3) == (1, 2, 4, 5, 6, 7)
assert extract_min_max((2, 3, 4, 8, 9, 11, 7), 4) == (2, 3, 4, 7, 8, 9, 11)
