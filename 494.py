'''Write a function to convert the given binary tuple to integer.
'''
def binary_to_integer(test_tup):
  res = int("".join(str(ele) for ele in test_tup), 2)
  return (str(res))
'''
Standard answer: 
def binary_to_integer(test_tup):
  res = int("".join(str(ele) for ele in test_tup), 2)
  return (str(res)) 
'''
assert binary_to_integer((1, 1, 0, 1, 0, 0, 1)) == '105'
assert binary_to_integer((0, 1, 1, 0, 0, 1, 0, 1)) == '101'
assert binary_to_integer((1, 1, 0, 1, 0, 1)) == '53'
