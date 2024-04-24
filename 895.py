'''Write a function to find the maximum sum of subsequences of given array with no adjacent elements.
'''
def max_sum_subseq(A):
    n = len(A)
    if n == 1:
        return A[0]
    look_up = [None] * n
    look_up[0] = A[0]
    look_up[1] = max(A[0], A[1])
    for i in range(2, n):
        look_up[i] = max(look_up[i - 1], look_up[i - 2] + A[i])
        look_up[i] = max(look_up[i], A[i])
    return look_up[n - 1]
'''
Standard answer: 
def max_sum_subseq(A):
    n = len(A)
    if n == 1:
        return A[0]
    look_up = [None] * n
    look_up[0] = A[0]
    look_up[1] = max(A[0], A[1])
    for i in range(2, n):
        look_up[i] = max(look_up[i - 1], look_up[i - 2] + A[i])
        look_up[i] = max(look_up[i], A[i])
    return look_up[n - 1]
'''
assert max_sum_subseq([1, 2, 9, 4, 5, 0, 4, 11, 6]) == 26
assert max_sum_subseq([1, 2, 9, 5, 6, 0, 5, 12, 7]) == 28
assert max_sum_subseq([1, 3, 10, 5, 6, 0, 6, 14, 21]) == 44
