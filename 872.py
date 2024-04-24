'''Write a function to check if a nested list is a subset of another nested list.
'''
def check_subset(list1,list2):
    for i in list2:
        if i not in list1:
            return False
    return True
'''
Standard answer: 
def check_subset(list1,list2): 
    return all(map(list1.__contains__,list2)) 
'''
assert check_subset([[1, 3], [5, 7], [9, 11], [13, 15, 17]] ,[[1, 3],[13,15,17]])==True
assert check_subset([[1, 2], [2, 3], [3, 4], [5, 6]],[[3, 4], [5, 6]])==True
assert check_subset([[[1, 2], [2, 3]], [[3, 4], [5, 7]]],[[[3, 4], [5, 6]]])==False
