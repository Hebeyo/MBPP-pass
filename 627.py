'''Write a python function to find the smallest missing number from the given array.
'''
def find_First_Missing(array,start,end): 
    if (start > end): 
        return end + 1
    if (start != array[start]): 
        return start; 
    mid = int((start + end) / 2) 
    if (array[mid] == mid): 
        return find_First_Missing(array,mid+1,end) 
    return find_First_Missing(array,start,mid)
'''
Standard answer: 
def find_First_Missing(array,start,end): 
    if (start > end): 
        return end + 1
    if (start != array[start]): 
        return start; 
    mid = int((start + end) / 2) 
    if (array[mid] == mid): 
        return find_First_Missing(array,mid+1,end) 
    return find_First_Missing(array,start,mid) 
'''
assert find_First_Missing([0,1,2,3],0,3) == 4
assert find_First_Missing([0,1,2,6,9],0,4) == 3
assert find_First_Missing([2,3,5,8,9],0,4) == 0
