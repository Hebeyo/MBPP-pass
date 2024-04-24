'''Write a function to generate a square matrix filled with elements from 1 to n raised to the power of 2 in spiral order.
'''
def generate_matrix(n):
    if n==0:
        return []
    if n==1:
        return [[1]]
    matrix = [[0 for i in range(n)] for j in range(n)]
    row_start = 0
    row_end = n-1
    col_start = 0
    col_end = n-1
    num = 1
    while row_start <= row_end and col_start <= col_end:
        for i in range(col_start, col_end+1):
            matrix[row_start][i] = num
            num += 1
        row_start += 1
        for i in range(row_start, row_end+1):
            matrix[i][col_end] = num
            num += 1
        col_end -= 1
        for i in range(col_end, col_start-1, -1):
            matrix[row_end][i] = num
            num += 1
        row_end -= 1
        for i in range(row_end, row_start-1, -1):
            matrix[i][col_start] = num
            num += 1
        col_start += 1
    return matrix
'''
Standard answer: 
def generate_matrix(n):
        if n<=0:
            return [] 
        matrix=[row[:] for row in [[0]*n]*n]        
        row_st=0
        row_ed=n-1        
        col_st=0
        col_ed=n-1
        current=1        
        while (True):
            if current>n*n:
                break
            for c in range (col_st, col_ed+1):
                matrix[row_st][c]=current
                current+=1
            row_st+=1
            for r in range (row_st, row_ed+1):
                matrix[r][col_ed]=current
                current+=1
            col_ed-=1
            for c in range (col_ed, col_st-1, -1):
                matrix[row_ed][c]=current
                current+=1
            row_ed-=1
            for r in range (row_ed, row_st-1, -1):
                matrix[r][col_st]=current
                current+=1
            col_st+=1
        return matrix
'''
assert generate_matrix(3)==[[1, 2, 3], [8, 9, 4], [7, 6, 5]] 
assert generate_matrix(2)==[[1,2],[4,3]]
assert generate_matrix(7)==[[1, 2, 3, 4, 5, 6, 7], [24, 25, 26, 27, 28, 29, 8], [23, 40, 41, 42, 43, 30, 9], [22, 39, 48, 49, 44, 31, 10], [21, 38, 47, 46, 45, 32, 11], [20, 37, 36, 35, 34, 33, 12], [19, 18, 17, 16, 15, 14, 13]]
