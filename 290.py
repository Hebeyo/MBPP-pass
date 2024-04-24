'''Write a function to find the list of lists with maximum length.
'''
def max_length(list1):
    max_length = 0
    max_list = []
    for i in list1:
        if len(i) > max_length:
            max_length = len(i)
            max_list = i
    return (max_length, max_list)
'''
Standard answer: 
def max_length(list1):
    max_length = max(len(x) for x in  list1 )  
    max_list = max((x) for x in   list1)
    return(max_length, max_list)
'''
assert max_length([[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]])==(3, [13, 15, 17])
assert max_length([[1], [5, 7], [10, 12, 14,15]])==(4, [10, 12, 14,15])
assert max_length([[5], [15,20,25]])==(3, [15,20,25])
