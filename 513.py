'''Write a function to convert tuple into list by adding the given string after every element.
'''
def add_str(test_tup, K):
  res = [ele for sub in test_tup for ele in (sub, K)]
  return (res)
'''
Standard answer: 
def add_str(test_tup, K):
  res = [ele for sub in test_tup for ele in (sub, K)]
  return (res) 
'''
assert add_str((5, 6, 7, 4, 9) , "FDF") == [5, 'FDF', 6, 'FDF', 7, 'FDF', 4, 'FDF', 9, 'FDF']
assert add_str((7, 8, 9, 10) , "PF") == [7, 'PF', 8, 'PF', 9, 'PF', 10, 'PF']
assert add_str((11, 14, 12, 1, 4) , "JH") == [11, 'JH', 14, 'JH', 12, 'JH', 1, 'JH', 4, 'JH']
