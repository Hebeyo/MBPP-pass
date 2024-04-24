'''Write a function to count unique keys for each value present in the tuple.
'''
def get_unique(test_list):
  res = {}
  for sub in test_list:
    if sub[1] in res:
      res[sub[1]].append(sub[0])
    else:
      res[sub[1]] = [sub[0]]
  res_dict = {}
  for key in res:
    res_dict[key] = len(set(res[key]))
  return (str(res_dict))
'''
Standard answer: 
from collections import defaultdict 
def get_unique(test_list):
  res = defaultdict(list)
  for sub in test_list:
    res[sub[1]].append(sub[0])
  res = dict(res)
  res_dict = dict()
  for key in res:
    res_dict[key] = len(list(set(res[key])))
  return (str(res_dict)) 
'''
assert get_unique([(3, 4), (1, 2), (2, 4), (8, 2), (7, 2), (8, 1), (9, 1), (8, 4), (10, 4)] ) == '{4: 4, 2: 3, 1: 2}'
assert get_unique([(4, 5), (2, 3), (3, 5), (9, 3), (8, 3), (9, 2), (10, 2), (9, 5), (11, 5)] ) == '{5: 4, 3: 3, 2: 2}'
assert get_unique([(6, 5), (3, 4), (2, 6), (11, 1), (8, 22), (8, 11), (4, 3), (14, 3), (11, 6)] ) == '{5: 1, 4: 1, 6: 2, 1: 1, 22: 1, 11: 1, 3: 2}'
