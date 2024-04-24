'''Write a function to check if a triangle of positive area is possible with the given angles.
'''
def is_triangleexists(a,b,c):
    if(a != 0 and b != 0 and c != 0 and (a + b + c)== 180):
        if((a + b)>= c or (b + c)>= a or (a + c)>= b):
            return True
        else:
            return False
    else:
        return False
'''
Standard answer: 
def is_triangleexists(a,b,c): 
    if(a != 0 and b != 0 and c != 0 and (a + b + c)== 180): 
        if((a + b)>= c or (b + c)>= a or (a + c)>= b): 
            return True 
        else:
            return False
    else:
        return False
'''
assert is_triangleexists(50,60,70)==True
assert is_triangleexists(90,45,45)==True
assert is_triangleexists(150,30,70)==False
