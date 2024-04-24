'''Write a function to remove tuple elements that occur more than once and replace the duplicates with some custom value.
'''
def remove_replica(test_tup):
  temp = set()
  res = tuple(ele if ele not in temp and not temp.add(ele) 
				else 'MSP' for ele in test_tup)
  return (res)
'''
Standard answer: 
def remove_replica(test_tup):
  temp = set()
  res = tuple(ele if ele not in temp and not temp.add(ele) 
				else 'MSP' for ele in test_tup)
  return (res)
'''
assert remove_replica((1, 1, 4, 4, 4, 5, 5, 6, 7, 7)) == (1, 'MSP', 4, 'MSP', 'MSP', 5, 'MSP', 6, 7, 'MSP')
assert remove_replica((2, 3, 4, 4, 5, 6, 6, 7, 8, 9, 9)) == (2, 3, 4, 'MSP', 5, 6, 'MSP', 7, 8, 9, 'MSP')
assert remove_replica((2, 2, 5, 4, 5, 7, 5, 6, 7, 7)) == (2, 'MSP', 5, 4, 'MSP', 7, 'MSP', 6, 'MSP', 'MSP')
