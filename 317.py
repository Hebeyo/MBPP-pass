'''Write a function to reflect the modified run-length encoding from a list.
'''
def modified_encode(alist):
    result = []
    i = 0
    while i < len(alist):
        count = 1
        while i+1 < len(alist) and alist[i] == alist[i+1]:
            i += 1
            count += 1
        if count > 1:
            result.append([count, alist[i]])
        else:
            result.append(alist[i])
        i += 1
    return result

'''
Standard answer: 
from itertools import groupby
def modified_encode(alist):
        def ctr_ele(el):
            if len(el)>1: return [len(el), el[0]]
            else: return el[0]
        return [ctr_ele(list(group)) for key, group in groupby(alist)]
'''
assert modified_encode([1,1,2,3,4,4,5,1])==[[2, 1], 2, 3, [2, 4], 5, 1]
assert modified_encode('automatically')==['a', 'u', 't', 'o', 'm', 'a', 't', 'i', 'c', 'a', [2, 'l'], 'y']
assert modified_encode('python')==['p', 'y', 't', 'h', 'o', 'n']
