'''Write a function to get dictionary keys as a list.
'''
def get_key(dict):
    list = []
    for key in dict.keys():
        list.append(key)
    return list
'''
Standard answer: 
def get_key(dict): 
    list = [] 
    for key in dict.keys(): 
        list.append(key)           
    return list
'''
assert get_key({1:'python',2:'java'})==[1,2]
assert get_key({10:'red',20:'blue',30:'black'})==[10,20,30]
assert get_key({27:'language',39:'java',44:'little'})==[27,39,44]
