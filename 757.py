'''Write a function to count the pairs of reverse strings in the given string list.
'''
def count_reverse_pairs(test_list):
  res = 0
  for idx in range(0, len(test_list)):
    for idxn in range(idx, len(test_list)):
      if test_list[idxn] == str(''.join(list(reversed(test_list[idx])))):
        res += 1
  return str(res)
'''
Standard answer: 
def count_reverse_pairs(test_list):
  res = sum([1 for idx in range(0, len(test_list)) for idxn in range(idx, len( 
	test_list)) if test_list[idxn] == str(''.join(list(reversed(test_list[idx]))))]) 
  return str(res)
'''
assert count_reverse_pairs(["julia", "best", "tseb", "for", "ailuj"])== '2'
assert count_reverse_pairs(["geeks", "best", "for", "skeeg"]) == '1'
assert count_reverse_pairs(["makes", "best", "sekam", "for", "rof"]) == '2' 
