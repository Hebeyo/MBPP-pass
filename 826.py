'''Write a python function to find the type of triangle from the given sides.
'''
def check_Type_Of_Triangle(a,b,c): 
    if (a**2 == a**2 + b**2 or b**2 == a**2 + c**2 or c**2 == a**2 + b**2): 
        return ("Right-angled Triangle") 
    elif (a**2 > c**2 + b**2 or b**2 > a**2 + c**2 or c**2 > a**2 + b**2): 
        return ("Obtuse-angled Triangle") 
    else: 
        return ("Acute-angled Triangle")
'''
Standard answer: 
def check_Type_Of_Triangle(a,b,c): 
    sqa = pow(a,2) 
    sqb = pow(b,2) 
    sqc = pow(c,2) 
    if (sqa == sqa + sqb or sqb == sqa + sqc or sqc == sqa + sqb): 
        return ("Right-angled Triangle") 
    elif (sqa > sqc + sqb or sqb > sqa + sqc or sqc > sqa + sqb): 
        return ("Obtuse-angled Triangle") 
    else: 
        return ("Acute-angled Triangle") 
'''
assert check_Type_Of_Triangle(1,2,3) == "Obtuse-angled Triangle"
assert check_Type_Of_Triangle(2,2,2) == "Acute-angled Triangle"
assert check_Type_Of_Triangle(1,0,1) == "Right-angled Triangle"
