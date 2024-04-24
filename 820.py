'''Write a function to check whether the given month number contains 28 days or not.
'''
def check_monthnum_number(monthnum1):
  if monthnum1 == 2:
    return True
  else:
    return False
'''
Standard answer: 
def check_monthnum_number(monthnum1):
  if monthnum1 == 2:
    return True
  else:
    return False
'''
assert check_monthnum_number(2)==True
assert check_monthnum_number(1)==False
assert check_monthnum_number(3)==False
