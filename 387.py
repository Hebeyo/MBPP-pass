'''Write a python function to check whether the hexadecimal number is even or odd.
'''
def even_or_odd(N): 
    l = len(N) 
    if (N[l-1] =='0'or N[l-1] =='2'or 
        N[l-1] =='4'or N[l-1] =='6'or 
        N[l-1] =='8'or N[l-1] =='A'or 
        N[l-1] =='C'or N[l-1] =='E'): 
        return ("Even") 
    else: 
        return ("Odd")
'''
Standard answer: 
def even_or_odd(N): 
    l = len(N) 
    if (N[l-1] =='0'or N[l-1] =='2'or 
        N[l-1] =='4'or N[l-1] =='6'or 
        N[l-1] =='8'or N[l-1] =='A'or 
        N[l-1] =='C'or N[l-1] =='E'): 
        return ("Even") 
    else: 
        return ("Odd") 
'''
assert even_or_odd("AB3454D") =="Odd"
assert even_or_odd("ABC") == "Even"
assert even_or_odd("AAD") == "Odd"
