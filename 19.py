'''Write a function to find whether a given array of integers contains any duplicate element.
'''
def test_duplicate(arraynums):
    for i in range(len(arraynums)):
        for j in range(i+1,len(arraynums)):
            if arraynums[i]==arraynums[j]:
                return True
    return False
'''
Standard answer: 
def test_duplicate(arraynums):
    nums_set = set(arraynums)    
    return len(arraynums) != len(nums_set)     
'''
assert test_duplicate(([1,2,3,4,5]))==False
assert test_duplicate(([1,2,3,4, 4]))==True
assert test_duplicate([1,1,2,2,3,3,4,4,5])==True
