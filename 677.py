'''Write a function to check if the triangle is valid or not.
'''
def validity_triangle(a,b,c):
    if a+b+c==180:
        return True
    else:
        return False
'''
Standard answer: 
def validity_triangle(a,b,c):
 total = a + b + c
 if total == 180:
    return True
 else:
    return False
'''
assert validity_triangle(60,50,90)==False
assert validity_triangle(45,75,60)==True
assert validity_triangle(30,50,100)==True
