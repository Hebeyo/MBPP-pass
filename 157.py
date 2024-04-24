'''Write a function to reflect the run-length encoding from a list.
'''
def encode_list(list1):
    result = []
    count = 1
    for i in range(1,len(list1)):
        if list1[i] == list1[i-1]:
            count += 1
        else:
            result.append([count, list1[i-1]])
            count = 1
    result.append([count, list1[-1]])
    return result
'''
Standard answer: 
from itertools import groupby
def encode_list(list1):
    return [[len(list(group)), key] for key, group in groupby(list1)]
'''
assert encode_list([1,1,2,3,4,4.3,5,1])==[[2, 1], [1, 2], [1, 3], [1, 4], [1, 4.3], [1, 5], [1, 1]]
assert encode_list('automatically')==[[1, 'a'], [1, 'u'], [1, 't'], [1, 'o'], [1, 'm'], [1, 'a'], [1, 't'], [1, 'i'], [1, 'c'], [1, 'a'], [2, 'l'], [1, 'y']]
assert encode_list('python')==[[1, 'p'], [1, 'y'], [1, 't'], [1, 'h'], [1, 'o'], [1, 'n']]
