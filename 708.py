'''Write a python function to convert a string to a list.
'''
def Convert(string):
    li = list(string.split(" "))
    return li
'''
Standard answer: 
def Convert(string): 
    li = list(string.split(" ")) 
    return li 
'''
assert Convert('python program') == ['python','program']
assert Convert('Data Analysis') ==['Data','Analysis']
assert Convert('Hadoop Training') == ['Hadoop','Training']
