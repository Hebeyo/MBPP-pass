'''Write a function to calculate the maximum aggregate from the list of tuples.
'''
def max_aggregate(stdata):
    temp = {}
    for name, marks in stdata:
        if name not in temp:
            temp[name] = marks
        else:
            temp[name] += marks
    max_aggregate = max(temp, key=temp.get)
    return (max_aggregate, temp[max_aggregate])
'''
Standard answer: 
from collections import defaultdict
def max_aggregate(stdata):
    temp = defaultdict(int)
    for name, marks in stdata:
        temp[name] += marks
    return max(temp.items(), key=lambda x: x[1])
'''
assert max_aggregate([('Juan Whelan',90),('Sabah Colley',88),('Peter Nichols',7),('Juan Whelan',122),('Sabah Colley',84)])==('Juan Whelan', 212)
assert max_aggregate([('Juan Whelan',50),('Sabah Colley',48),('Peter Nichols',37),('Juan Whelan',22),('Sabah Colley',14)])==('Juan Whelan', 72)
assert max_aggregate([('Juan Whelan',10),('Sabah Colley',20),('Peter Nichols',30),('Juan Whelan',40),('Sabah Colley',50)])==('Sabah Colley', 70)
