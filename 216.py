'''Write a function to check if a nested list is a subset of another nested list.
'''
def check_subset_list(list1, list2):
    l1, l2 = list1[0], list2[0]
    exist = True
    for i in list2:
        if i not in list1:
            exist = False
    return exist
'''
Standard answer: 
def check_subset_list(list1, list2): 
    l1, l2 = list1[0], list2[0] 
    exist = True
    for i in list2: 
        if i not in list1: 
            exist = False
    return exist 
'''
assert check_subset_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14],[[12, 18, 23, 25, 45], [7, 11, 19, 24, 28], [1, 5, 8, 18, 15, 16]])==False
assert check_subset_list([[2, 3, 1], [4, 5], [6, 8]],[[4, 5], [6, 8]])==True
assert check_subset_list([['a', 'b'], ['e'], ['c', 'd']],[['g']])==False
