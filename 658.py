'''Write a function to find the item with maximum occurrences in a given list.
'''
def max_occurrences(list1):
    max_val = 0
    result = list1[0] 
    for i in list1:
        occu = list1.count(i)
        if occu > max_val:
            max_val = occu
            result = i 
    return result
'''
Standard answer: 
def max_occurrences(list1):
    max_val = 0
    result = list1[0] 
    for i in list1:
        occu = list1.count(i)
        if occu > max_val:
            max_val = occu
            result = i 
    return result
'''
assert max_occurrences([2,3,8,4,7,9,8,2,6,5,1,6,1,2,3,4,6,9,1,2])==2
assert max_occurrences([1, 3,5, 7,1, 3,13, 15, 17,5, 7,9,1, 11])==1
assert max_occurrences([1, 2, 3,2, 4, 5,1, 1, 1])==1
