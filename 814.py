'''Write a function to find the area of a rombus.
'''
def rombus_area(p,q):
  return p*q/2
'''
Standard answer: 
def rombus_area(p,q):
  area=(p*q)/2
  return area
'''
assert rombus_area(10,20)==100
assert rombus_area(10,5)==25
assert rombus_area(4,2)==4
