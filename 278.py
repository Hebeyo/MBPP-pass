'''Write a function to find the element count that occurs before the record in the given tuple.
'''
def count_first_elements(test_tup):
  count = 0
  for ele in test_tup:
    if isinstance(ele, tuple):
      break
    count += 1
  return (count)
'''
Standard answer: 
def count_first_elements(test_tup):
  for count, ele in enumerate(test_tup):
    if isinstance(ele, tuple):
      break
  return (count) 
'''
assert count_first_elements((1, 5, 7, (4, 6), 10) ) == 3
assert count_first_elements((2, 9, (5, 7), 11) ) == 2
assert count_first_elements((11, 15, 5, 8, (2, 3), 8) ) == 4
