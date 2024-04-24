'''Write a function to round the given number to the nearest multiple of a specific number.
'''
def round_num(n,m):
    a = (n //m) * m
    b = a + m
    if n - a > b - n:
        return b
    else:
        return a
'''
Standard answer: 
def round_num(n,m):
    a = (n //m) * m
    b = a + m
    return (b if n - a > b - n else a)
'''
assert round_num(4722,10)==4720
assert round_num(1111,5)==1110
assert round_num(219,2)==218
