'''Write a function to find all index positions of the maximum values in a given list.
'''
def position_max(list1):
    max_val = max(list1)
    max_result = [i for i, j in enumerate(list1) if j == max_val]
    return max_result
'''
Standard answer: 
def position_max(list1):
    max_val = max(list1)
    max_result = [i for i, j in enumerate(list1) if j == max_val]
    return max_result
'''
assert position_max([12,33,23,10,67,89,45,667,23,12,11,10,54])==[7]
assert position_max([1,2,2,2,4,4,4,5,5,5,5])==[7,8,9,10]
assert position_max([2,1,5,6,8,3,4,9,10,11,8,12])==[11]
