'''Write a python function to remove even numbers from a given list.
'''
def remove_even(l):
    return [i for i in l if i%2!=0]
'''
Standard answer: 
def remove_even(l):
    for i in l:
        if i % 2 == 0:
            l.remove(i)
    return l
'''
assert remove_even([1,3,5,2]) == [1,3,5]
assert remove_even([5,6,7]) == [5,7]
assert remove_even([1,2,3,4]) == [1,3]
