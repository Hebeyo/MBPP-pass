'''Write a python function to check whether an array contains only one distinct element or not.
'''
def unique_Element(arr,n):
    if len(set(arr)) == 1:
        return ('YES')
    else:
        return ('NO')
'''
Standard answer: 
def unique_Element(arr,n):
    s = set(arr)
    if (len(s) == 1):
        return ('YES')
    else:
        return ('NO')
'''
assert unique_Element([1,1,1],3) == 'YES'
assert unique_Element([1,2,1,2],4) == 'NO'
assert unique_Element([1,2,3,4,5],5) == 'NO'
