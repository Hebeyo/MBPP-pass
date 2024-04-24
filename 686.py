'''Write a function to find the frequency of each element in the given list.
'''
def freq_element(test_tup):
  res = {}
  for ele in test_tup:
    if ele in res:
      res[ele] += 1
    else:
      res[ele] = 1
  return (str(res))
'''
Standard answer: 
from collections import defaultdict 
def freq_element(test_tup):
  res = defaultdict(int)
  for ele in test_tup:
    res[ele] += 1
  return (str(dict(res))) 
'''
assert freq_element((4, 5, 4, 5, 6, 6, 5, 5, 4) ) == '{4: 3, 5: 4, 6: 2}'
assert freq_element((7, 8, 8, 9, 4, 7, 6, 5, 4) ) == '{7: 2, 8: 2, 9: 1, 4: 2, 6: 1, 5: 1}'
assert freq_element((1, 4, 3, 1, 4, 5, 2, 6, 2, 7) ) == '{1: 2, 4: 2, 3: 1, 5: 1, 2: 2, 6: 1, 7: 1}'
