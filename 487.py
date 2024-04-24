'''Write a function to sort a list of tuples in increasing order by the last element in each tuple.
'''
def sort_tuple(tup):
  return sorted(tup, key=lambda x: x[-1])
'''
Standard answer: 
def sort_tuple(tup): 
	lst = len(tup) 
	for i in range(0, lst): 
		for j in range(0, lst-i-1): 
			if (tup[j][-1] > tup[j + 1][-1]): 
				temp = tup[j] 
				tup[j]= tup[j + 1] 
				tup[j + 1]= temp 
	return tup
'''
assert sort_tuple([(1, 3), (3, 2), (2, 1)] ) == [(2, 1), (3, 2), (1, 3)]
assert sort_tuple([(2, 4), (3, 3), (1, 1)] ) == [(1, 1), (3, 3), (2, 4)]
assert sort_tuple([(3, 9), (6, 7), (4, 3)] ) == [(4, 3), (6, 7), (3, 9)]
