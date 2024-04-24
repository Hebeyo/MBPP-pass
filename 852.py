'''Write a python function to remove negative numbers from a list.
'''
def remove_negs(num_list): 
    for item in num_list: 
        if item < 0: 
            num_list.remove(item) 
    return num_list
'''
Standard answer: 
def remove_negs(num_list): 
    for item in num_list: 
        if item < 0: 
           num_list.remove(item) 
    return num_list
'''
assert remove_negs([1,-2,3,-4]) == [1,3]
assert remove_negs([1,2,3,-4]) == [1,2,3]
assert remove_negs([4,5,-6,7,-8]) == [4,5,7]
