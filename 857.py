'''Write a function to list out the list of given strings individually using map function.
'''
def listify_list(list1):
  result = list(map(list,list1)) 
  return result
'''
Standard answer: 
def listify_list(list1):
  result = list(map(list,list1)) 
  return result 
'''
assert listify_list(['Red', 'Blue', 'Black', 'White', 'Pink'])==[['R', 'e', 'd'], ['B', 'l', 'u', 'e'], ['B', 'l', 'a', 'c', 'k'], ['W', 'h', 'i', 't', 'e'], ['P', 'i', 'n', 'k']]
assert listify_list(['python'])==[['p', 'y', 't', 'h', 'o', 'n']]
assert listify_list([' red ', 'green',' black', 'blue ',' orange', 'brown'])==[[' ', 'r', 'e', 'd', ' '], ['g', 'r', 'e', 'e', 'n'], [' ', 'b', 'l', 'a', 'c', 'k'], ['b', 'l', 'u', 'e', ' '], [' ', 'o', 'r', 'a', 'n', 'g', 'e'], ['b', 'r', 'o', 'w', 'n']]
