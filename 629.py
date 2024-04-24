'''Write a python function to find even numbers from a mixed list.
'''
def Split(list): 
    ev_li = [] 
    for i in list: 
        if (i % 2 == 0): 
            ev_li.append(i)  
    return ev_li
'''
Standard answer: 
def Split(list): 
    ev_li = [] 
    for i in list: 
        if (i % 2 == 0): 
            ev_li.append(i)  
    return ev_li
'''
assert Split([1,2,3,4,5]) == [2,4]
assert Split([4,5,6,7,8,0,1]) == [4,6,8,0]
assert Split ([8,12,15,19]) == [8,12]
