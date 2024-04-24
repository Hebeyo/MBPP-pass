'''Write a function to extract every specified element from a given two dimensional list.
'''
def specified_element(nums, N):
    result = []
    for i in nums:
        result.append(i[N])
    return result
'''
Standard answer: 
def specified_element(nums, N):
    result = [i[N] for i in nums]
    return result
'''
assert specified_element([[1, 2, 3, 2], [4, 5, 6, 2], [7, 1, 9, 5]],0)==[1, 4, 7]
assert specified_element([[1, 2, 3, 2], [4, 5, 6, 2], [7, 1, 9, 5]],2)==[3, 6, 9]
assert specified_element([[1, 2, 3, 2], [4, 5, 6, 2], [7, 1, 9, 5]],3)==[2,2,5]
