'''Write a function to print check if the triangle is isosceles or not.
'''
def check_isosceles(x,y,z):
  if x==y or y==z or z==x:
	   return True
  else:
     return False
'''
Standard answer: 
def check_isosceles(x,y,z):
  if x==y or y==z or z==x:
	   return True
  else:
     return False
'''
assert check_isosceles(6,8,12)==False 
assert check_isosceles(6,6,12)==True
assert check_isosceles(6,16,20)==False
