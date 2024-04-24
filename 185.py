'''Write a function to find the focus of a parabola.
'''
def parabola_focus(a, b, c):
  focus= (((-b / (2 * a)),(((4 * a * c) - (b * b) + 1) / (4 * a))))
  return focus
'''
Standard answer: 
def parabola_focus(a, b, c): 
  focus= (((-b / (2 * a)),(((4 * a * c) - (b * b) + 1) / (4 * a))))
  return focus
'''
assert parabola_focus(5,3,2)==(-0.3, 1.6)
assert parabola_focus(9,8,4)==(-0.4444444444444444, 2.25)
assert parabola_focus(2,4,6)==(-1.0, 4.125)
