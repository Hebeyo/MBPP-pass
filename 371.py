'''Write a function to find the smallest missing element in a sorted array.
'''
def smallest_missing(A, left_element, right_element):
    if left_element > right_element:
        return left_element
    mid = left_element + (right_element - left_element) // 2
    if A[mid] == mid:
        return smallest_missing(A, mid + 1, right_element)
    else:
        return smallest_missing(A, left_element, mid - 1)
'''
Standard answer: 
def smallest_missing(A, left_element, right_element):
    if left_element > right_element:
        return left_element
    mid = left_element + (right_element - left_element) // 2
    if A[mid] == mid:
        return smallest_missing(A, mid + 1, right_element)
    else:
        return smallest_missing(A, left_element, mid - 1)
'''
assert smallest_missing([0, 1, 2, 3, 4, 5, 6], 0, 6) == 7
assert smallest_missing([0, 1, 2, 6, 9, 11, 15], 0, 6) == 3
assert smallest_missing([1, 2, 3, 4, 6, 9, 11, 15], 0, 7) == 0
