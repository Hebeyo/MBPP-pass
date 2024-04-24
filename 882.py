'''Write a function to caluclate perimeter of a parallelogram.
'''
def parallelogram_perimeter(b,h):
  return 2*(b*h)
'''
Standard answer: 
def parallelogram_perimeter(b,h):
  perimeter=2*(b*h)
  return perimeter
'''
assert parallelogram_perimeter(10,20)==400
assert parallelogram_perimeter(15,20)==600
assert parallelogram_perimeter(8,9)==144
