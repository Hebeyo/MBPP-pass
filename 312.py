'''Write a function to find the volume of a cone.
'''
def volume_cone(r,h):
  volume = (1.0/3) * 3.141592653589793238 * r * r * h
  return volume
'''
Standard answer: 
import math
def volume_cone(r,h):
  volume = (1.0/3) * math.pi * r * r * h
  return volume
'''
assert volume_cone(5,12)==314.15926535897927
assert volume_cone(10,15)==1570.7963267948965
assert volume_cone(19,17)==6426.651371693521
