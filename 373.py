'''Write a function to find the volume of a cuboid.
'''
def volume_cuboid(l,w,h):
  volume=l*w*h
  return volume
'''
Standard answer: 
def volume_cuboid(l,w,h):
  volume=l*w*h
  return volume
'''
assert volume_cuboid(1,2,3)==6
assert volume_cuboid(5,7,9)==315
assert volume_cuboid(10,15,21)==3150
