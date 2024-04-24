'''Write a function to insert a given string at the beginning of all items in a list.
'''
def add_string(list,string):
 add_string=[string.format(i) for i in  list]
 return add_string
'''
Standard answer: 
def add_string(list,string):
 add_string=[string.format(i) for i in  list]
 return add_string
'''
assert add_string([1,2,3,4],'temp{0}')==['temp1', 'temp2', 'temp3', 'temp4']
assert add_string(['a','b','c','d'], 'python{0}')==[ 'pythona', 'pythonb', 'pythonc', 'pythond']
assert add_string([5,6,7,8],'string{0}')==['string5', 'string6', 'string7', 'string8']
