'''Write a function to pack consecutive duplicates of a given list elements into sublists.
'''
def pack_consecutive_duplicates(list1):
    res = []
    temp = [list1[0]]
    for i in range(1, len(list1)):
        if list1[i] == list1[i - 1]:
            temp.append(list1[i])
        else:
            res.append(temp)
            temp = [list1[i]]
    res.append(temp)
    return res
'''
Standard answer: 
from itertools import groupby
def pack_consecutive_duplicates(list1):
    return [list(group) for key, group in groupby(list1)]
'''
assert pack_consecutive_duplicates([0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4])==[[0, 0], [1], [2], [3], [4, 4], [5], [6, 6, 6], [7], [8], [9], [4, 4]]
assert pack_consecutive_duplicates([10, 10, 15, 19, 18, 18, 17, 26, 26, 17, 18, 10])==[[10, 10], [15], [19], [18, 18], [17], [26, 26], [17], [18], [10]]
assert pack_consecutive_duplicates(['a', 'a', 'b', 'c', 'd', 'd'])==[['a', 'a'], ['b'], ['c'], ['d', 'd']]
