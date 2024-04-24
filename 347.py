'''Write a python function to count the number of squares in a rectangle.
'''
def count_Squares(m,n): 
    if (n < m): 
        temp = m 
        m = n 
        n = temp 
    return n * (n + 1) * (3 * m - n + 1) // 6
'''
Standard answer: 
def count_Squares(m,n): 
    if (n < m): 
        temp = m 
        m = n 
        n = temp 
    return n * (n + 1) * (3 * m - n + 1) // 6
'''
assert count_Squares(4,3) == 20
assert count_Squares(1,2) == 2
assert count_Squares(2,2) == 5
