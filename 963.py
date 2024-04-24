'''Write a function to calculate the discriminant value.
'''
def discriminant_value(x,y,z):
    discriminant = (y**2) - (4*x*z)
    if discriminant > 0:
        return ("Two solutions",discriminant)
    elif discriminant == 0:
        return ("one solution",discriminant)
    elif discriminant < 0:
        return ("no real solution",discriminant)
'''
Standard answer: 
def discriminant_value(x,y,z):
    discriminant = (y**2) - (4*x*z)
    if discriminant > 0:
        return ("Two solutions",discriminant)
    elif discriminant == 0:
        return ("one solution",discriminant)
    elif discriminant < 0:
        return ("no real solution",discriminant)
'''
assert discriminant_value(4,8,2)==("Two solutions",32)
assert discriminant_value(5,7,9)==("no real solution",-131)
assert discriminant_value(0,0,9)==("one solution",0)
