'''Write a function to check if each element of second tuple is smaller than its corresponding index in first tuple.
'''
def check_smaller(test_tup1, test_tup2):
  for i in range(len(test_tup1)):
    if test_tup1[i] < test_tup2[i]:
      return False
  return True
'''
Standard answer: 
def check_smaller(test_tup1, test_tup2):
  res = all(x > y for x, y in zip(test_tup1, test_tup2))
  return (res) 
'''
assert check_smaller((1, 2, 3), (2, 3, 4)) == False
assert check_smaller((4, 5, 6), (3, 4, 5)) == True
assert check_smaller((11, 12, 13), (10, 11, 12)) == True
