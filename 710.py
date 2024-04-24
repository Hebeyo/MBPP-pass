'''Write a function to access the initial and last data of the given tuple record.
'''
def front_and_rear(test_tup):
  res = (test_tup[0], test_tup[-1])
  return (res)
'''
Standard answer: 
def front_and_rear(test_tup):
  res = (test_tup[0], test_tup[-1])
  return (res) 
'''
assert front_and_rear((10, 4, 5, 6, 7)) == (10, 7)
assert front_and_rear((1, 2, 3, 4, 5)) == (1, 5)
assert front_and_rear((6, 7, 8, 9, 10)) == (6, 10)
