'''Write a function to find the perimeter of a pentagon.
'''
def perimeter_pentagon(a):
  perimeter=(5*a)
  return perimeter
'''
Standard answer: 
import math
def perimeter_pentagon(a):
  perimeter=(5*a)
  return perimeter
'''
assert perimeter_pentagon(5)==25
assert perimeter_pentagon(10)==50
assert perimeter_pentagon(15)==75
