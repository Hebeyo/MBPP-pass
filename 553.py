'''Write a function to convert the given tuple to a floating-point number.
'''
def tuple_to_float(test_tup):
  res = float('.'.join(str(ele) for ele in test_tup))
  return (res)
'''
Standard answer: 
def tuple_to_float(test_tup):
  res = float('.'.join(str(ele) for ele in test_tup))
  return (res) 
'''
assert tuple_to_float((4, 56)) == 4.56
assert tuple_to_float((7, 256)) == 7.256
assert tuple_to_float((8, 123)) == 8.123
