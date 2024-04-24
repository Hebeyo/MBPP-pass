'''Write a function for nth catalan number.
'''
def catalan_number(n): 
    if n <= 1: 
        return 1
    res = 0
    for i in range(n): 
        res += catalan_number(i) * catalan_number(n-i-1)
    return res
'''
Standard answer: 
def catalan_number(num):
    if num <=1:
         return 1   
    res_num = 0
    for i in range(num):
        res_num += catalan_number(i) * catalan_number(num-i-1)
    return res_num
'''
assert catalan_number(10)==16796
assert catalan_number(9)==4862
assert catalan_number(7)==429
