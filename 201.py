'''Write a python function to check whether the elements in a list are same or not.
'''
def chkList(lst):
    for i in range(len(lst)):
        for j in range(i+1,len(lst)):
            if lst[i] != lst[j]:
                return False
    return True
'''
Standard answer: 
def chkList(lst): 
    return len(set(lst)) == 1
'''
assert chkList(['one','one','one']) == True
assert chkList(['one','Two','Three']) == False
assert chkList(['bigdata','python','Django']) == False
