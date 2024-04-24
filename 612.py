'''Write a python function to merge the first and last elements separately in a list of lists.
'''
def merge(lst):
    result = []
    for i in range(len(lst[0])):
        temp = []
        for j in range(len(lst)):
            temp.append(lst[j][i])
        result.append(temp)
    return result
'''
Standard answer: 
def merge(lst):  
    return [list(ele) for ele in list(zip(*lst))] 
'''
assert merge([['x', 'y'], ['a', 'b'], ['m', 'n']]) == [['x', 'a', 'm'], ['y', 'b', 'n']]
assert merge([[1, 2], [3, 4], [5, 6], [7, 8]]) == [[1, 3, 5, 7], [2, 4, 6, 8]]
assert merge([['x', 'y','z' ], ['a', 'b','c'], ['m', 'n','o']]) == [['x', 'a', 'm'], ['y', 'b', 'n'],['z', 'c','o']]
