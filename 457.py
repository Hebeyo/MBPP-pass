'''Write a python function to find the sublist having minimum length.
'''
def Find_Min(lst):
    minList = min((x) for x in lst)
    return minList
'''
Standard answer: 
def Find_Min(lst): 
    minList = min((x) for x in lst) 
    return minList
'''
assert Find_Min([[1],[1,2],[1,2,3]]) == [1]
assert Find_Min([[1,1],[1,1,1],[1,2,7,8]]) == [1,1]
assert Find_Min([['x'],['x','y'],['x','y','z']]) == ['x']
