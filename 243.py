'''Write a function to sort the given list based on the occurrence of first element of tuples.
'''
def sort_on_occurence(lst):
  dct = {}
  for i, j in lst:
    dct.setdefault(i, []).append(j)
  return ([(i, *dict.fromkeys(j), len(j)) for i, j in dct.items()])
'''
Standard answer: 
def sort_on_occurence(lst): 
	dct = {} 
	for i, j in lst: 
		dct.setdefault(i, []).append(j) 
	return ([(i, *dict.fromkeys(j), len(j)) 
				for i, j in dct.items()]) 
'''
assert sort_on_occurence([(1, 'Jake'), (2, 'Bob'), (1, 'Cara')]) == [(1, 'Jake', 'Cara', 2), (2, 'Bob', 1)]
assert sort_on_occurence([('b', 'ball'), ('a', 'arm'), ('b', 'b'), ('a', 'ant')]) == [('b', 'ball', 'b', 2), ('a', 'arm', 'ant', 2)]
assert sort_on_occurence([(2, 'Mark'), (3, 'Maze'), (2, 'Sara')]) == [(2, 'Mark', 'Sara', 2), (3, 'Maze', 1)]
