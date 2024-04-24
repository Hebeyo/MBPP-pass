'''Write a function to find the surface area of a cuboid.
'''
def surfacearea_cuboid(l,w,h):
  SA = 2*(l*w + l * h + w * h)
  return SA
'''
Standard answer: 
def surfacearea_cuboid(l,w,h):
  SA = 2*(l*w + l * h + w * h)
  return SA
'''
assert surfacearea_cuboid(1,2,3)==22
assert surfacearea_cuboid(5,7,9)==286
assert surfacearea_cuboid(10,15,21)==1350
