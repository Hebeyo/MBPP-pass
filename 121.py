'''Write a function to find the triplet with sum of the given array
'''
def check_triplet(A, n, sum, count):
    if count == 3 and sum == 0:
        return True
    if count == 3 or n == 0 or sum < 0:
        return False
    return check_triplet(A, n - 1, sum - A[n - 1], count + 1) or\
           check_triplet(A, n - 1, sum, count)
'''
Standard answer: 
def check_triplet(A, n, sum, count):
    if count == 3 and sum == 0:
        return True
    if count == 3 or n == 0 or sum < 0:
        return False
    return check_triplet(A, n - 1, sum - A[n - 1], count + 1) or\
           check_triplet(A, n - 1, sum, count)
'''
assert check_triplet([2, 7, 4, 0, 9, 5, 1, 3], 8, 6, 0) == True
assert check_triplet([1, 4, 5, 6, 7, 8, 5, 9], 8, 6, 0) == False
assert check_triplet([10, 4, 2, 3, 5], 5, 15, 0) == True
