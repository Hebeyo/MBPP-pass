'''Write a function to count the number of unique lists within a list.
'''
def unique_sublists(list1):
    result = {}
    for l in list1:
        result.setdefault(tuple(l), list()).append(1)
    for a, b in result.items():
        result[a] = sum(b)
    return result
'''
Standard answer: 
def unique_sublists(list1):
    result ={}
    for l in list1: 
        result.setdefault(tuple(l), list()).append(1) 
    for a, b in result.items(): 
        result[a] = sum(b)
    return result
'''
assert unique_sublists([[1, 3], [5, 7], [1, 3], [13, 15, 17], [5, 7], [9, 11]])=={(1, 3): 2, (5, 7): 2, (13, 15, 17): 1, (9, 11): 1}
assert unique_sublists([['green', 'orange'], ['black'], ['green', 'orange'], ['white']])=={('green', 'orange'): 2, ('black',): 1, ('white',): 1}
assert unique_sublists([[1, 2], [3, 4], [4, 5], [6, 7]])=={(1, 2): 1, (3, 4): 1, (4, 5): 1, (6, 7): 1}
