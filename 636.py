'''Write a python function to check if roots of a quadratic equation are reciprocal of each other or not.
'''
def Check_Solution(a,b,c):
    if (a == c):
        return ("Yes")
    else:
        return ("No")
'''
Standard answer: 
def Check_Solution(a,b,c): 
    if (a == c): 
        return ("Yes"); 
    else: 
        return ("No"); 
'''
assert Check_Solution(2,0,2) == "Yes"
assert Check_Solution(2,-5,2) == "Yes"
assert Check_Solution(1,2,3) == "No"
