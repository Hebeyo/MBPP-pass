'''Write a python function to set all odd bits of a given number.
'''
def odd_bit_set_number(n):
    count = 0;res = 0;temp = n
    while temp > 0:
        if count % 2 == 0:
            res |= (1 << count)
        count += 1
        temp >>= 1
    return (n | res)
'''
Standard answer: 
def odd_bit_set_number(n):
    count = 0;res = 0;temp = n
    while temp > 0:
        if count % 2 == 0:
            res |= (1 << count)
        count += 1
        temp >>= 1
    return (n | res)
'''
assert odd_bit_set_number(10) == 15
assert odd_bit_set_number(20) == 21
assert odd_bit_set_number(30) == 31
