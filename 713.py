'''Write a function to check if the given tuple contains all valid values or not.
'''
def check_valid(test_tup):
  res = not any(map(lambda ele: not ele, test_tup))
  return (res)
'''
Standard answer: 
def check_valid(test_tup):
  res = not any(map(lambda ele: not ele, test_tup))
  return (res) 
'''
assert check_valid((True, True, True, True) ) == True
assert check_valid((True, False, True, True) ) == False
assert check_valid((True, True, True, True) ) == True
