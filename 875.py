'''Write a function to find the minimum difference in the tuple pairs of given tuples.
'''
def min_difference(test_list):
  temp = [abs(b - a) for a, b in test_list]
  res = min(temp)
  return (res)
'''
Standard answer: 
def min_difference(test_list):
  temp = [abs(b - a) for a, b in test_list]
  res = min(temp)
  return (res) 
'''
assert min_difference([(3, 5), (1, 7), (10, 3), (1, 2)]) == 1
assert min_difference([(4, 6), (12, 8), (11, 4), (2, 13)]) == 2
assert min_difference([(5, 17), (3, 9), (12, 5), (3, 24)]) == 6
