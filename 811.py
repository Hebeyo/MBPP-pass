'''Write a function to check if two lists of tuples are identical or not.
'''
def check_identical(test_list1, test_list2):
  for i in range(len(test_list1)):
    if test_list1[i] != test_list2[i]:
      return False
  return True
'''
Standard answer: 
def check_identical(test_list1, test_list2):
  res = test_list1 == test_list2
  return (res) 
'''
assert check_identical([(10, 4), (2, 5)], [(10, 4), (2, 5)]) == True
assert check_identical([(1, 2), (3, 7)], [(12, 14), (12, 45)]) == False
assert check_identical([(2, 14), (12, 25)], [(2, 14), (12, 25)]) == True
