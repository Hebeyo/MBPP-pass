'''Write a function to check whether the given month name contains 30 days or not.
'''
def check_monthnumber(monthname3):
  if monthname3 =="April" or monthname3== "June" or monthname3== "September" or monthname3== "November":
    return True
  else:
    return False
'''
Standard answer: 
def check_monthnumber(monthname3):
  if monthname3 =="April" or monthname3== "June" or monthname3== "September" or monthname3== "November":
    return True
  else:
    return False
'''
assert check_monthnumber("February")==False
assert check_monthnumber("June")==True
assert check_monthnumber("April")==True
