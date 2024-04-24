'''Write a function to find the area of a trapezium.
'''
def area_trapezium(base1,base2,height):
 area = 0.5 * (base1 + base2) * height
 return area
'''
Standard answer: 
def area_trapezium(base1,base2,height):
 area = 0.5 * (base1 + base2) * height
 return area
'''
assert area_trapezium(6,9,4)==30
assert area_trapezium(10,20,30)==450
assert area_trapezium(15,25,35)==700
