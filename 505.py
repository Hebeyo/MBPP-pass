'''Write a function to move all zeroes to the end of the given array.
'''
def re_order(A):
    k = 0
    for i in A:
        if i:
            A[k] = i
            k = k + 1
    for i in range(k, len(A)):
        A[i] = 0
    return A
'''
Standard answer: 
def re_order(A):
    k = 0
    for i in A:
        if i:
            A[k] = i
            k = k + 1
    for i in range(k, len(A)):
        A[i] = 0
    return A
'''
assert re_order([6, 0, 8, 2, 3, 0, 4, 0, 1]) == [6, 8, 2, 3, 4, 1, 0, 0, 0]
assert re_order([4, 0, 2, 7, 0, 9, 0, 12, 0]) == [4, 2, 7, 9, 12, 0, 0, 0, 0]
assert re_order([3, 11, 0, 74, 14, 0, 1, 0, 2]) == [3, 11, 74, 14, 1, 2, 0, 0, 0]
