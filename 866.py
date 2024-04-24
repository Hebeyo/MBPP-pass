'''Write a function to check whether the given month name contains 31 days or not.
'''
def check_monthnumb(monthname2):
  if(monthname2=="January" or monthname2=="March"or monthname2=="May" or monthname2=="July" or monthname2=="Augest" or monthname2=="October" or monthname2=="December"):
    return True
  else:
    return False
'''
Standard answer: 
def check_monthnumb(monthname2):
  if(monthname2=="January" or monthname2=="March"or monthname2=="May" or monthname2=="July" or monthname2=="Augest" or monthname2=="October" or monthname2=="December"):
    return True
  else:
    return False
'''
assert check_monthnumb("February")==False
assert check_monthnumb("January")==True
assert check_monthnumb("March")==True
