'''Write a python function to check whether the value exists in a sequence or not.
'''
def overlapping(list1,list2):
    for i in list1:
        for j in list2:
            if i==j:
                return True
    else:
        return False
'''
Standard answer: 
def overlapping(list1,list2):  
    c=0
    d=0
    for i in list1: 
        c+=1
    for i in list2: 
        d+=1
    for i in range(0,c): 
        for j in range(0,d): 
            if(list1[i]==list2[j]): 
                return 1
    return 0
'''
assert overlapping([1,2,3,4,5],[6,7,8,9]) == False
assert overlapping([1,2,3],[4,5,6]) == False
assert overlapping([1,4,5],[1,4,5]) == True
