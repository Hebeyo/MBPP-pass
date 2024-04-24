'''Write a function to sum a specific column of a list in a given list of lists.
'''
def sum_column(list1, C):
    result = 0
    for row in list1:
        result += row[C]
    return result
'''
Standard answer: 
def sum_column(list1, C):
    result = sum(row[C] for row in list1)
    return result
'''
assert sum_column( [[1,2,3,2],[4,5,6,2],[7,8,9,5],],0)==12
assert sum_column( [[1,2,3,2],[4,5,6,2],[7,8,9,5],],1)==15
assert sum_column( [[1,2,3,2],[4,5,6,2],[7,8,9,5],],3)==9
