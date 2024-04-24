'''Write a python function to convert a list of multiple integers into a single integer.
'''
def convert(list):
    num = 0
    for i in range(len(list)):
        num = num*10 + list[i]
    return num
'''
Standard answer: 
def convert(list): 
    s = [str(i) for i in list] 
    res = int("".join(s))  
    return (res) 
'''
assert convert([1,2,3]) == 123
assert convert([4,5,6]) == 456
assert convert([7,8,9]) == 789
