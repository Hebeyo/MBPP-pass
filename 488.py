'''Write a function to find the area of a pentagon.
'''
import math
def area_pentagon(a):
  area=(math.sqrt(5*(5+2*math.sqrt(5)))*pow(a,2))/4.0
  return area
'''
Standard answer: 
import math
def area_pentagon(a):
  area=(math.sqrt(5*(5+2*math.sqrt(5)))*pow(a,2))/4.0
  return area
'''
assert area_pentagon(5)==43.01193501472417
assert area_pentagon(10)==172.0477400588967
assert area_pentagon(15)==387.10741513251753
