'''Write a function to sort a given matrix in ascending order according to the sum of its rows.
'''
def sort_matrix(M):
    n = len(M)
    for i in range(n):
        for j in range(n-i-1):
            if sum(M[j]) > sum(M[j+1]):
                M[j], M[j+1] = M[j+1], M[j]
    return M
'''
Standard answer: 
def sort_matrix(M):
    result = sorted(M, key=sum)
    return result
'''
assert sort_matrix([[1, 2, 3], [2, 4, 5], [1, 1, 1]])==[[1, 1, 1], [1, 2, 3], [2, 4, 5]]
assert sort_matrix([[1, 2, 3], [-2, 4, -5], [1, -1, 1]])==[[-2, 4, -5], [1, -1, 1], [1, 2, 3]]
assert sort_matrix([[5,8,9],[6,4,3],[2,1,4]])==[[2, 1, 4], [6, 4, 3], [5, 8, 9]]
