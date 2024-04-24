'''Write a function to caluclate arc length of an angle.
'''
def arc_length(d,a):
    pi=22/7
    if a >= 360:
        return None
    arclength = (pi*d) * (a/360)
    return arclength
'''
Standard answer: 
def arc_length(d,a):
    pi=22/7
    if a >= 360:
        return None
    arclength = (pi*d) * (a/360)
    return arclength
'''
assert arc_length(9,45)==3.5357142857142856
assert arc_length(9,480)==None
assert arc_length(5,270)==11.785714285714285
