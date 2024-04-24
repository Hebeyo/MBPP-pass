'''Write a function to check if any list element is present in the given list.
'''
def check_element(test_tup, check_list):
  res = False
  for ele in check_list:
    if ele in test_tup:
      res = True
      break
  return (res)
'''
Standard answer: 
def check_element(test_tup, check_list):
  res = False
  for ele in check_list:
    if ele in test_tup:
      res = True
      break
  return (res) 
'''
assert check_element((4, 5, 7, 9, 3),  [6, 7, 10, 11]) == True
assert check_element((1, 2, 3, 4),  [4, 6, 7, 8, 9]) == True
assert check_element((3, 2, 1, 4, 5),  [9, 8, 7, 6]) == False
