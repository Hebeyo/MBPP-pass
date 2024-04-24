'''Write a function to extract the sum of alternate chains of tuples.
'''
def sum_of_alternates(test_tuple):
  sum1 = 0
  sum2 = 0
  for idx, ele in enumerate(test_tuple):
    if idx % 2:
      sum1 += ele
    else:
      sum2 += ele
  return ((sum1),(sum2))
'''
Standard answer: 
def sum_of_alternates(test_tuple):
  sum1 = 0
  sum2 = 0
  for idx, ele in enumerate(test_tuple):
    if idx % 2:
      sum1 += ele
    else:
      sum2 += ele
  return ((sum1),(sum2)) 
'''
assert sum_of_alternates((5, 6, 3, 6, 10, 34)) == (46, 18)
assert sum_of_alternates((1, 2, 3, 4, 5)) == (6, 9)
assert sum_of_alternates((6, 7, 8, 9, 4, 5)) == (21, 18)
