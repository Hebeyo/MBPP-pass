'''Write a function to calculate volume of a tetrahedron.
'''
def volume_tetrahedron(num):
	volume = (num ** 3 / (6 * 2**0.5))	
	return round(volume, 2)
'''
Standard answer: 
import math
def volume_tetrahedron(num):
	volume = (num ** 3 / (6 * math.sqrt(2)))	
	return round(volume, 2)
'''
assert volume_tetrahedron(10)==117.85
assert volume_tetrahedron(15)==397.75
assert volume_tetrahedron(20)==942.81
