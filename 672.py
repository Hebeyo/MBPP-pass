'''Write a function to find maximum of three numbers.
'''
def max_of_three(num1,num2,num3): 
    if (num1 >= num2) and (num1 >= num3):
       lnum = num1
    elif (num2 >= num1) and (num2 >= num3):
       lnum = num2
    else:
       lnum = num3
    return lnum
'''
Standard answer: 
def max_of_three(num1,num2,num3): 
    if (num1 >= num2) and (num1 >= num3):
       lnum = num1
    elif (num2 >= num1) and (num2 >= num3):
       lnum = num2
    else:
       lnum = num3
    return lnum
'''
assert max_of_three(10,20,30)==30
assert max_of_three(55,47,39)==55
assert max_of_three(10,49,30)==49
