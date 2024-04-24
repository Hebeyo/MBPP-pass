'''Write a function to find the volume of a cylinder.
'''
def volume_cylinder(r,h):
  volume=3.1415*r*r*h
  return volume
'''
Standard answer: 
def volume_cylinder(r,h):
  volume=3.1415*r*r*h
  return volume
'''
assert volume_cylinder(10,5)==1570.7500000000002
assert volume_cylinder(4,5)==251.32000000000002
assert volume_cylinder(4,10)==502.64000000000004
