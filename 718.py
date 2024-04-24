'''Write a function to create a list taking alternate elements from another given list.
'''
def alternate_elements(list1):
    result=[]
    for i in range(0, len(list1), 2):
        result.append(list1[i])
    return result
'''
Standard answer: 
def alternate_elements(list1):
    result=[]
    for item in list1[::2]:
        result.append(item)
    return result 
'''
assert alternate_elements(["red", "black", "white", "green", "orange"])==['red', 'white', 'orange']
assert alternate_elements([2, 0, 3, 4, 0, 2, 8, 3, 4, 2])==[2, 3, 0, 8, 4]
assert alternate_elements([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])==[1,3,5,7,9]
