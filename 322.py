'''Write a function to find all index positions of the minimum values in a given list.
'''
def position_min(list1):
    min_val = min(list1)
    min_result = [i for i, j in enumerate(list1) if j == min_val]
    return min_result
'''
Standard answer: 
def position_min(list1):
    min_val = min(list1)
    min_result = [i for i, j in enumerate(list1) if j == min_val]
    return min_result
'''
assert position_min([12,33,23,10,67,89,45,667,23,12,11,10,54])==[3,11]
assert position_min([1,2,2,2,4,4,4,5,5,5,5])==[0]
assert position_min([2,1,5,6,8,3,4,9,10,11,8,12])==[1]
