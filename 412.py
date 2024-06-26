'''Write a python function to remove odd numbers from a given list.
'''
def remove_odd(l):
    i = 0
    while i < len(l):
        if l[i] % 2 != 0:
            l.pop(i)
        else:
            i += 1
    return l
'''
Standard answer: 
def remove_odd(l):
    for i in l:
        if i % 2 != 0:
            l.remove(i)
    return l
'''
assert remove_odd([1,2,3]) == [2]
assert remove_odd([2,4,6]) == [2,4,6]
assert remove_odd([10,20,3]) == [10,20]
