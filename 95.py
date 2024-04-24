'''Write a python function to find the minimum length of sublist.
'''
def Find_Min_Length(lst):
    minLength = len(lst[0])
    for i in range(1,len(lst)):
        if len(lst[i]) < minLength:
            minLength = len(lst[i])
    return minLength
'''
Standard answer: 
def Find_Min_Length(lst):  
    minLength = min(len(x) for x in lst )
    return minLength 
'''
assert Find_Min_Length([[1],[1,2]]) == 1
assert Find_Min_Length([[1,2],[1,2,3],[1,2,3,4]]) == 2
assert Find_Min_Length([[3,3,3],[4,4,4,4]]) == 3
