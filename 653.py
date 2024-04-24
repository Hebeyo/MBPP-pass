'''Write a function to group a sequence of key-value pairs into a dictionary of lists using collections module.
'''
def grouping_dictionary(l):
    d = {}
    for k, v in l:
        if k in d:
            d[k].append(v)
        else:
            d[k] = [v]
    return d
'''
Standard answer: 
from collections import defaultdict
def grouping_dictionary(l):
    d = defaultdict(list)
    for k, v in l:
        d[k].append(v)
    return d
'''
assert grouping_dictionary([('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)])== ({'yellow': [1, 3], 'blue': [2, 4], 'red': [1]})
assert grouping_dictionary([('yellow', 10), ('blue', 20), ('yellow', 30), ('blue', 40), ('red', 10)])== ({'yellow': [10, 30], 'blue': [20, 40], 'red': [10]})
assert grouping_dictionary([('yellow', 15), ('blue', 25), ('yellow', 35), ('blue', 45), ('red', 15)])== ({'yellow': [15, 35], 'blue': [25, 45], 'red': [15]})
