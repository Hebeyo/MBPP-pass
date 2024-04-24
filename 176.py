'''Write a function to find the perimeter of a triangle.
'''
def perimeter_triangle(a,b,c):
  perimeter=a+b+c
  return perimeter
'''
Standard answer: 
def perimeter_triangle(a,b,c):
  perimeter=a+b+c
  return perimeter
'''
assert perimeter_triangle(10,20,30)==60
assert perimeter_triangle(3,4,5)==12
assert perimeter_triangle(25,35,45)==105
