'''Write a python function to count the number of squares in a rectangle.
'''
def count_Squares(m,n):
    if(n < m):
        temp = m
        m = n
        n = temp
    return ((m * (m + 1) * (2 * m + 1) / 6 + (n - m) * m * (m + 1) / 2))
'''
Standard answer: 
def count_Squares(m,n):
    if(n < m):
        temp = m
        m = n
        n = temp
    return ((m * (m + 1) * (2 * m + 1) / 6 + (n - m) * m * (m + 1) / 2))
'''
assert count_Squares(4,3) == 20
assert count_Squares(2,2) == 5
assert count_Squares(1,1) == 1
