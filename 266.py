'''Write a function to find the lateral surface area of a cube.
'''
def lateralsurface_cube(l):
  LSA = 4 * (l * l)
  return LSA
'''
Standard answer: 
def lateralsurface_cube(l):
  LSA = 4 * (l * l)
  return LSA
'''
assert lateralsurface_cube(5)==100
assert lateralsurface_cube(9)==324
assert lateralsurface_cube(10)==400
