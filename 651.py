'''Write a function to check if one tuple is a subset of another tuple.
'''
def check_subset(test_tup1, test_tup2):
  res = set(test_tup2).issubset(set(test_tup1))
  return (res)
'''
Standard answer: 
def check_subset(test_tup1, test_tup2):
  res = set(test_tup2).issubset(test_tup1)
  return (res) 
'''
assert check_subset((10, 4, 5, 6), (5, 10)) == True
assert check_subset((1, 2, 3, 4), (5, 6)) == False
assert check_subset((7, 8, 9, 10), (10, 8)) == True
