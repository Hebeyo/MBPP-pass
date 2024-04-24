'''Write a python function to find number of solutions in quadratic equation.
'''
def Check_Solution(a,b,c) : 
    if ((b*b) - (4*a*c)) > 0 : 
        return ("2 solutions") 
    elif ((b*b) - (4*a*c)) == 0 : 
        return ("1 solution") 
    else : 
        return ("No solutions")
'''
Standard answer: 
def Check_Solution(a,b,c) : 
    if ((b*b) - (4*a*c)) > 0 : 
        return ("2 solutions") 
    elif ((b*b) - (4*a*c)) == 0 : 
        return ("1 solution") 
    else : 
        return ("No solutions") 
'''
assert Check_Solution(2,5,2) == "2 solutions"
assert Check_Solution(1,1,1) == "No solutions"
assert Check_Solution(1,2,1) == "1 solution"
