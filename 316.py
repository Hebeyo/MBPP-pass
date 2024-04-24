'''Write a function to find the index of the last occurrence of a given number in a sorted array.
'''
def find_last_occurrence(A, x):
    (left, right) = (0, len(A) - 1)
    result = -1
    while left <= right:
        mid = (left + right) // 2
        if x == A[mid]:
            result = mid
            left = mid + 1
        elif x < A[mid]:
            right = mid - 1
        else:
            left = mid + 1
    return result
'''
Standard answer: 
def find_last_occurrence(A, x):
    (left, right) = (0, len(A) - 1)
    result = -1
    while left <= right:
        mid = (left + right) // 2
        if x == A[mid]:
            result = mid
            left = mid + 1
        elif x < A[mid]:
            right = mid - 1
        else:
            left = mid + 1
    return result 
'''
assert find_last_occurrence([2, 5, 5, 5, 6, 6, 8, 9, 9, 9], 5) == 3
assert find_last_occurrence([2, 3, 5, 8, 6, 6, 8, 9, 9, 9], 9) == 9
assert find_last_occurrence([2, 2, 1, 5, 6, 6, 6, 9, 9, 9], 6) == 6
