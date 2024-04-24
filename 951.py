'''Write a function to find the maximum of similar indices in two lists of tuples.
'''
def max_similar_indices(test_list1, test_list2):
  res = [(max(x[0], y[0]), max(x[1], y[1]))
   for x, y in zip(test_list1, test_list2)]
  return (res)
'''
Standard answer: 
def max_similar_indices(test_list1, test_list2):
  res = [(max(x[0], y[0]), max(x[1], y[1]))
   for x, y in zip(test_list1, test_list2)]
  return (res) 
'''
assert max_similar_indices([(2, 4), (6, 7), (5, 1)],[(5, 4), (8, 10), (8, 14)]) == [(5, 4), (8, 10), (8, 14)]
assert max_similar_indices([(3, 5), (7, 8), (6, 2)],[(6, 5), (9, 11), (9, 15)]) == [(6, 5), (9, 11), (9, 15)]
assert max_similar_indices([(4, 6), (8, 9), (7, 3)],[(7, 6), (10, 12), (10, 16)]) == [(7, 6), (10, 12), (10, 16)]
