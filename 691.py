'''Write a function to group the 1st elements on the basis of 2nd elements in the given tuple list.
'''
def group_element(test_list):
  res = dict()
  test_list.sort(key = lambda ele: ele[1])
  for ele in test_list:
    if ele[1] in res:
      res[ele[1]].append(ele[0])
    else:
      res[ele[1]] = [ele[0]]
  return (res)
'''
Standard answer: 
from itertools import groupby 
def group_element(test_list):
  res = dict()
  for key, val in groupby(sorted(test_list, key = lambda ele: ele[1]), key = lambda ele: ele[1]):
    res[key] = [ele[0] for ele in val] 
  return (res)

'''
assert group_element([(6, 5), (2, 7), (2, 5), (8, 7), (9, 8), (3, 7)]) == {5: [6, 2], 7: [2, 8, 3], 8: [9]}
assert group_element([(7, 6), (3, 8), (3, 6), (9, 8), (10, 9), (4, 8)]) == {6: [7, 3], 8: [3, 9, 4], 9: [10]}
assert group_element([(8, 7), (4, 9), (4, 7), (10, 9), (11, 10), (5, 9)]) == {7: [8, 4], 9: [4, 10, 5], 10: [11]}
