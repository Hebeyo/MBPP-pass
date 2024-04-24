'''Write a function to check whether the given month name contains 28 days or not.
'''
def check_monthnum(monthname1):
  if monthname1 == "February":
    return True
  else:
    return False
'''
Standard answer: 
def check_monthnum(monthname1):
  if monthname1 == "February":
    return True
  else:
    return False
'''
assert check_monthnum("February")==True
assert check_monthnum("January")==False
assert check_monthnum("March")==False
