'''Write a function to count number of lists in a given list of lists and square the count.
'''
def count_list(input_list):
    return (len(input_list))**2
'''
Standard answer: 
def count_list(input_list): 
    return (len(input_list))**2
'''
assert count_list([[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]])==25
assert count_list([[1, 3], [5, 7], [9, 11], [13, 15, 17]] )==16
assert count_list([[2, 4], [[6,8], [4,5,8]], [10, 12, 14]])==9
