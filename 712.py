'''Write a function to remove duplicates from a list of lists.
'''
def remove_duplicate(list1):
    list1.sort()
    remove_duplicate = []
    for i in list1:
        if i not in remove_duplicate:
            remove_duplicate.append(i)
    return remove_duplicate
'''
Standard answer: 
import itertools
def remove_duplicate(list1):
 list.sort(list1)
 remove_duplicate = list(list1 for list1,_ in itertools.groupby(list1))
 return remove_duplicate
'''
assert remove_duplicate([[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]])==[[10, 20], [30, 56, 25], [33], [40]] 
assert remove_duplicate(["a", "b", "a", "c", "c"] )==["a", "b", "c"]
assert remove_duplicate([1, 3, 5, 6, 3, 5, 6, 1] )==[1, 3, 5, 6]
