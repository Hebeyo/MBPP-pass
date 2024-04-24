'''Write a function to remove a specified column from a given nested list.
'''
def remove_column(list1, n):
  for i in list1: 
    del i[n] 
  return list1
'''
Standard answer: 
def remove_column(list1, n):
   for i in list1: 
    del i[n] 
   return list1
'''
assert remove_column([[1, 2, 3], [2, 4, 5], [1, 1, 1]],0)==[[2, 3], [4, 5], [1, 1]]
assert remove_column([[1, 2, 3], [-2, 4, -5], [1, -1, 1]],2)==[[1, 2], [-2, 4], [1, -1]]
assert remove_column([[1, 3], [5, 7], [1, 3], [13, 15, 17], [5, 7], [9, 11]],0)==[[3], [7], [3], [15, 17], [7], [11]]
