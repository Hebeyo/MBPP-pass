'''Write a function to re-arrange the given tuples based on the given ordered list.
'''
def re_arrange_tuples(test_list, ord_list):
  temp = dict(test_list)
  res = [(key, temp[key]) for key in ord_list]
  return (res)
'''
Standard answer: 
def re_arrange_tuples(test_list, ord_list):
  temp = dict(test_list)
  res = [(key, temp[key]) for key in ord_list]
  return (res) 
'''
assert re_arrange_tuples([(4, 3), (1, 9), (2, 10), (3, 2)],  [1, 4, 2, 3]) == [(1, 9), (4, 3), (2, 10), (3, 2)]
assert re_arrange_tuples([(5, 4), (2, 10), (3, 11), (4, 3)],  [3, 4, 2, 3]) == [(3, 11), (4, 3), (2, 10), (3, 11)]
assert re_arrange_tuples([(6, 3), (3, 8), (5, 7), (2, 4)],  [2, 5, 3, 6]) == [(2, 4), (5, 7), (3, 8), (6, 3)]
