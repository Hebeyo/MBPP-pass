'''Write a function to sort the given tuple list basis the total digits in tuple.
'''
def sort_list(test_list):
  test_list.sort(key = lambda i: len(str(i)))
  return (str(test_list))
'''
Standard answer: 
def count_digs(tup):
  return sum([len(str(ele)) for ele in tup ]) 
def sort_list(test_list):
  test_list.sort(key = count_digs)
  return (str(test_list))
'''
assert sort_list([(3, 4, 6, 723), (1, 2), (12345,), (134, 234, 34)] ) == '[(1, 2), (12345,), (3, 4, 6, 723), (134, 234, 34)]'
assert sort_list([(3, 4, 8), (1, 2), (1234335,), (1345, 234, 334)] ) == '[(1, 2), (3, 4, 8), (1234335,), (1345, 234, 334)]'
assert sort_list([(34, 4, 61, 723), (1, 2), (145,), (134, 23)] ) == '[(1, 2), (145,), (134, 23), (34, 4, 61, 723)]'
