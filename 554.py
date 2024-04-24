'''Write a python function to find odd numbers from a mixed list.
'''
def Split(list):
  odd_list = []
  for i in list:
    if (i % 2 != 0):
      odd_list.append(i)  
  return odd_list
'''
Standard answer: 
def Split(list): 
    od_li = [] 
    for i in list: 
        if (i % 2 != 0): 
            od_li.append(i)  
    return od_li
'''
assert Split([1,2,3,4,5,6]) == [1,3,5]
assert Split([10,11,12,13]) == [11,13]
assert Split([7,8,9,1]) == [7,9,1]
