'''Write a function to sort each sublist of strings in a given list of lists.
'''
def sort_sublists(list1):
    result = []
    for i in range(len(list1)):
        list1[i] = sorted(list1[i])
        result.append(list1[i])
    return result
'''
Standard answer: 
def sort_sublists(list1):
    result = list(map(sorted,list1)) 
    return result
'''
assert sort_sublists([['green', 'orange'], ['black', 'white'], ['white', 'black', 'orange']])==[['green', 'orange'], ['black', 'white'], ['black', 'orange', 'white']]
assert sort_sublists([['green', 'orange'], ['black'], ['green', 'orange'], ['white']])==[['green', 'orange'], ['black'], ['green', 'orange'], ['white']]
assert sort_sublists([['a','b'],['d','c'],['g','h'] , ['f','e']])==[['a', 'b'], ['c', 'd'], ['g', 'h'], ['e', 'f']]
