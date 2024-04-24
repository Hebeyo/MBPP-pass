'''Write a python function to shift first element to the end of given list.
'''
def move_last(num_list):
    a = [num_list[0] for i in range(num_list.count(num_list[0]))]
    x = [ i for i in num_list if i != num_list[0]]
    x.extend(a)
    return (x)
'''
Standard answer: 
def move_last(num_list):
    a = [num_list[0] for i in range(num_list.count(num_list[0]))]
    x = [ i for i in num_list if i != num_list[0]]
    x.extend(a)
    return (x)
'''
assert move_last([1,2,3,4]) == [2,3,4,1]
assert move_last([2,3,4,1,5,0]) == [3,4,1,5,0,2]
assert move_last([5,4,3,2,1]) == [4,3,2,1,5]
