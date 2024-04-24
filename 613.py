'''Write a function to find the maximum value in record list as tuple attribute in the given tuple list.
'''
def maximum_value(test_list):
  res = []
  for i in test_list:
    res.append((i[0], max(i[1])))
  return (res)
'''
Standard answer: 
def maximum_value(test_list):
  res = [(key, max(lst)) for key, lst in test_list]
  return (res) 
'''
assert maximum_value([('key1', [3, 4, 5]), ('key2', [1, 4, 2]), ('key3', [9, 3])]) == [('key1', 5), ('key2', 4), ('key3', 9)]
assert maximum_value([('key1', [4, 5, 6]), ('key2', [2, 5, 3]), ('key3', [10, 4])]) == [('key1', 6), ('key2', 5), ('key3', 10)]
assert maximum_value([('key1', [5, 6, 7]), ('key2', [3, 6, 4]), ('key3', [11, 5])]) == [('key1', 7), ('key2', 6), ('key3', 11)]
