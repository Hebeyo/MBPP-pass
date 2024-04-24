'''Write a function to join the tuples if they have similar initial elements.
'''
def join_tuples(test_list):
  res = []
  for sub in test_list:
    if res and res[-1][0] == sub[0]:
      res[-1].extend(sub[1:])
    else:
      res.append([ele for ele in sub])
  res = list(map(tuple, res))
  return (res)
'''
Standard answer: 
def join_tuples(test_list):
  res = []
  for sub in test_list:
    if res and res[-1][0] == sub[0]:
      res[-1].extend(sub[1:])
    else:
      res.append([ele for ele in sub])
  res = list(map(tuple, res))
  return (res) 
'''
assert join_tuples([(5, 6), (5, 7), (6, 8), (6, 10), (7, 13)] ) == [(5, 6, 7), (6, 8, 10), (7, 13)]
assert join_tuples([(6, 7), (6, 8), (7, 9), (7, 11), (8, 14)] ) == [(6, 7, 8), (7, 9, 11), (8, 14)]
assert join_tuples([(7, 8), (7, 9), (8, 10), (8, 12), (9, 15)] ) == [(7, 8, 9), (8, 10, 12), (9, 15)]
