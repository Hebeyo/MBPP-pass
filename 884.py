'''Write a python function to check whether all the bits are within a given range or not.
'''
def all_Bits_Set_In_The_Given_Range(n,l,r):
    for i in range(l, r+1):
        if (n & (1 << (i-1))) == 0:
            return False
    return True
'''
Standard answer: 
def all_Bits_Set_In_The_Given_Range(n,l,r): 
    num = ((1 << r) - 1) ^ ((1 << (l - 1)) - 1) 
    new_num = n & num 
    if (num == new_num): 
        return True
    return False
'''
assert all_Bits_Set_In_The_Given_Range(10,2,1) == True 
assert all_Bits_Set_In_The_Given_Range(5,2,4) == False
assert all_Bits_Set_In_The_Given_Range(22,2,3) == True 
