'''Write a python function to find the maximum volume of a cuboid with given sum of sides.
'''
def max_volume (s): 
    maxvalue = 0
    i = 1
    for i in range(s - 1): 
        j = 1
        for j in range(s): 
            k = s - i - j 
            maxvalue = max(maxvalue, i * j * k)         
    return maxvalue
'''
Standard answer: 
def max_volume (s): 
    maxvalue = 0
    i = 1
    for i in range(s - 1): 
        j = 1
        for j in range(s): 
            k = s - i - j 
            maxvalue = max(maxvalue, i * j * k)         
    return maxvalue 
'''
assert max_volume(8) == 18
assert max_volume(4) == 2
assert max_volume(1) == 0
