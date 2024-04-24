'''Write a python function to find the largest postive number from the given list.
'''
def largest_pos(list1):
    max = list1[0]
    for x in list1:
        if x > max:
            max = x
    return max
'''
Standard answer: 
def largest_pos(list1): 
    max = list1[0] 
    for x in list1: 
        if x > max : 
             max = x  
    return max
'''
assert largest_pos([1,2,3,4,-1]) == 4
assert largest_pos([0,1,2,-5,-1,6]) == 6
assert largest_pos([0,0,1,0]) == 1
