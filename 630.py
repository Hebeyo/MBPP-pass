'''Write a function to extract all the adjacent coordinates of the given coordinate tuple.
'''
def get_coordinates(test_tup):
  res = []
  for i in range(test_tup[0]-1, test_tup[0]+2):
    for j in range(test_tup[1]-1, test_tup[1]+2):
      res.append([i,j])
  return res
'''
Standard answer: 
def adjac(ele, sub = []): 
  if not ele: 
     yield sub 
  else: 
     yield from [idx for j in range(ele[0] - 1, ele[0] + 2) 
                for idx in adjac(ele[1:], sub + [j])] 
def get_coordinates(test_tup):
  res = list(adjac(test_tup))
  return (res) 
'''
assert get_coordinates((3, 4)) == [[2, 3], [2, 4], [2, 5], [3, 3], [3, 4], [3, 5], [4, 3], [4, 4], [4, 5]]
assert get_coordinates((4, 5)) ==[[3, 4], [3, 5], [3, 6], [4, 4], [4, 5], [4, 6], [5, 4], [5, 5], [5, 6]]
assert get_coordinates((5, 6)) == [[4, 5], [4, 6], [4, 7], [5, 5], [5, 6], [5, 7], [6, 5], [6, 6], [6, 7]]
