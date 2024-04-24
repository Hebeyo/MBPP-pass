'''Write a function to extract all the pairs which are symmetric in the given tuple list.
'''
def extract_symmetric(test_list):
  temp = set(test_list) & {(b, a) for a, b in test_list}
  res = {(a, b) for a, b in temp if a < b}
  return (res)
'''
Standard answer: 
def extract_symmetric(test_list):
  temp = set(test_list) & {(b, a) for a, b in test_list}
  res = {(a, b) for a, b in temp if a < b}
  return (res) 
'''
assert extract_symmetric([(6, 7), (2, 3), (7, 6), (9, 8), (10, 2), (8, 9)] ) == {(8, 9), (6, 7)}
assert extract_symmetric([(7, 8), (3, 4), (8, 7), (10, 9), (11, 3), (9, 10)] ) == {(9, 10), (7, 8)}
assert extract_symmetric([(8, 9), (4, 5), (9, 8), (11, 10), (12, 4), (10, 11)] ) == {(8, 9), (10, 11)}
