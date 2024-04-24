'''Write a function to rotate a given list by specified number of items to the right direction.
'''
def rotate_right(list1,m,n):
  result =  list1[-(m):]+list1[:-(n)]
  return result
'''
Standard answer: 
def rotate_right(list1,m,n):
  result =  list1[-(m):]+list1[:-(n)]
  return result
'''
assert rotate_right([1, 2, 3, 4, 5, 6, 7, 8, 9, 10],3,4)==[8, 9, 10, 1, 2, 3, 4, 5, 6]
assert rotate_right([1, 2, 3, 4, 5, 6, 7, 8, 9, 10],2,2)==[9, 10, 1, 2, 3, 4, 5, 6, 7, 8]
assert rotate_right([1, 2, 3, 4, 5, 6, 7, 8, 9, 10],5,2)==[6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8]
