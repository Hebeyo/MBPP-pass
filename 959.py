'''Write a python function to find the average of a list.
'''
def Average(lst): 
    return sum(lst) / len(lst)
'''
Standard answer: 
def Average(lst): 
    return sum(lst) / len(lst) 
'''
assert Average([15, 9, 55, 41, 35, 20, 62, 49]) == 35.75
assert Average([4, 5, 1, 2, 9, 7, 10, 8]) == 5.75
assert Average([1,2,3]) == 2
