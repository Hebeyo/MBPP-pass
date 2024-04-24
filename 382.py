'''Write a function to find the number of rotations in a circularly sorted array.
'''
def find_rotation_count(A):
    (left, right) = (0, len(A) - 1)
    while left <= right:
        if A[left] <= A[right]:
            return left
        mid = (left + right) // 2
        next = (mid + 1) % len(A)
        prev = (mid - 1 + len(A)) % len(A)
        if A[mid] <= A[next] and A[mid] <= A[prev]:
            return mid
        elif A[mid] <= A[right]:
            right = mid - 1
        elif A[mid] >= A[left]:
            left = mid + 1
    return -1
'''
Standard answer: 
def find_rotation_count(A):
    (left, right) = (0, len(A) - 1)
    while left <= right:
        if A[left] <= A[right]:
            return left
        mid = (left + right) // 2
        next = (mid + 1) % len(A)
        prev = (mid - 1 + len(A)) % len(A)
        if A[mid] <= A[next] and A[mid] <= A[prev]:
            return mid
        elif A[mid] <= A[right]:
            right = mid - 1
        elif A[mid] >= A[left]:
            left = mid + 1
    return -1
'''
assert find_rotation_count([8, 9, 10, 1, 2, 3, 4, 5, 6, 7]) == 3
assert find_rotation_count([8, 9, 10,2, 5, 6]) == 3
assert find_rotation_count([2, 5, 6, 8, 9, 10]) == 0
