'''Write a function to sort a given mixed list of integers and strings.
'''
def sort_mixed_list(mixed_list):
    int_part = []
    str_part = []
    for i in mixed_list:
        if type(i) is int:
            int_part.append(i)
        else:
            str_part.append(i)
    int_part.sort()
    str_part.sort()
    return int_part + str_part
'''
Standard answer: 
def sort_mixed_list(mixed_list):
    int_part = sorted([i for i in mixed_list if type(i) is int])
    str_part = sorted([i for i in mixed_list if type(i) is str])
    return int_part + str_part
'''
assert sort_mixed_list([19,'red',12,'green','blue', 10,'white','green',1])==[1, 10, 12, 19, 'blue', 'green', 'green', 'red', 'white']
assert sort_mixed_list([19,'red',12,'green','blue', 10,'white','green',1])==[1, 10, 12, 19, 'blue', 'green', 'green', 'red', 'white']
assert sort_mixed_list([19,'red',12,'green','blue', 10,'white','green',1])==[1, 10, 12, 19, 'blue', 'green', 'green', 'red', 'white']
